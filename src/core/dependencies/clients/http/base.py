from src.clients.http.base import BaseHttpClient


async def get_base_http_client() -> BaseHttpClient:
    """
    Construct a new BaseHttpClient instance.
    """
    return BaseHttpClient()
