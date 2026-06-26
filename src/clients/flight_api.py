from typing import Literal

from config.config import settings

from src.clients.http.base import BaseHttpClient


class FlightApiClient(BaseHttpClient):
    """
    Class to work with flightapi.io.
    """

    async def get_airport_data(
            self,
            airport_iata: str,
            mode: Literal["arrivals", "departures"],
    ) -> list[dict] | dict:
        """
        Get airport data and schedule based on it's IATA code.

        Details: https://api.flightapi.io/schedule
        """
        url = f"https://api.flightapi.io/schedule/{settings.flight_api.api_key}"
        params = {
            "iata": airport_iata,
            "mode": mode,
            "day": 1,
        }

        response = await self.get(url, params)
        return response.json()
