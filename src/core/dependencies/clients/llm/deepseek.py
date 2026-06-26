from fastapi import Depends

from src.clients.http.base import BaseHttpClient
from src.clients.llm.deepseek import DeepSeekClient
from src.core.dependencies.clients.http.base import get_base_http_client


async def get_deepseek_client(
        http_service: BaseHttpClient = Depends(get_base_http_client)
) -> DeepSeekClient:
    """
    Construct a new DeepSeekClient instance with injected dependencies.
    """
    return DeepSeekClient(http_service)
