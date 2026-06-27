from typing import Literal

from src.clients.flight_api import FlightApiClient
from src.clients.llm.deepseek import DeepSeekClient
from src.dto.airports import AirportData, Flight
from src.dto.questions import QuestionDTO
from src.static.prompts import airport_question


class FlightsService:
    def __init__(
            self,
            deepseek_client: DeepSeekClient,
            flights_api_client: FlightApiClient,
    ):
        self.deepseek_client = deepseek_client
        self.flights_api_client = flights_api_client

    async def ask_about_flight(self, question_data: QuestionDTO) -> str:
        """
        Ask a question about given flight to LLM.
        """
        airport_data = await self._get_airport_data(question_data.airport)

        prompt = airport_question % (
            question_data.question,
            airport_data.name,
            airport_data.flights,
        )
        return await self.deepseek_client.generate(prompt)

    async def _get_airport_data(
            self,
            airport_iata: str,
            mode: Literal["arrivals", "departures"] = "arrivals",
    ) -> AirportData:
        """
        Get airport data and schedule based on it's IATA code from FlightAPI.
        """
        raw_airport_data = await self.flights_api_client.get_airport_data(airport_iata, mode)
        schedule = await self._get_raw_schedule(raw_airport_data, mode)
        flights = [self._get_flight_dto(flight.get("flight")) for flight in schedule]

        return AirportData(
            flights=flights,
            name=raw_airport_data.get("airport").get("pluginData").get("details").get("name"),
        )

    async def _get_raw_schedule(
            self,
            raw_airport_data: dict,
            mode: Literal["arrivals", "departures"],
    ) -> list[dict]:
        """
        Extract airport schedule data from raw airport data.
        :param raw_airport_data: Raw airport data from https://api.flightapi.io/schedule
        :param mode: arrivals/departures
        :return: airport's schedule as list of flights in dictionary format
        """
        airport = raw_airport_data.get("airport")
        schedule = airport.get("pluginData").get("schedule")

        return schedule.get(mode).get("data")

    @staticmethod
    def _get_flight_dto(raw_flight: dict) -> Flight:
        """
        Format raw flight data to DTO model.
        """
        number = raw_flight.get("identification")
        airline = raw_flight.get("airline")
        origin = raw_flight.get("airport").get("origin").get("name")
        status = raw_flight.get("status").get("text")

        return Flight(
            number=number.get("number").get("default") if number else None,
            airline=airline.get("name") if airline else None,
            aircraft=raw_flight.get("aircraft").get("model").get("text"),
            origin=origin,
            status=status,
            time=raw_flight.get("time"),
        )
