from src.clients.flight_api import FlightApiClient


async def get_flight_api_client() -> FlightApiClient:
    """
    Construct a new FlightApiClient instance.
    """
    return FlightApiClient()
