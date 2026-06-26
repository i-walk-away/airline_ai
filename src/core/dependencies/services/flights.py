from fastapi import Depends

from src.clients.flight_api import FlightApiClient
from src.clients.llm.deepseek import DeepSeekClient
from src.core.dependencies.clients.flight_api import get_flight_api_client
from src.core.dependencies.clients.llm.deepseek import get_deepseek_client
from src.services.flights import FlightsService


async def get_flights_service(
        flight_api_client: FlightApiClient = Depends(get_flight_api_client),
        deepseek_client: DeepSeekClient = Depends(get_deepseek_client),
) -> FlightsService:
    """
    Construct a new FlightsService instance with injected dependencies.
    """
    return FlightsService(deepseek_client, flight_api_client)
