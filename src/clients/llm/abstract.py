from abc import ABC, abstractmethod

from src.clients.http.base import BaseHttpClient


class AbstractLlmClient(ABC):
    def __init__(self, http_service: BaseHttpClient):
        self.http_service = http_service

    @abstractmethod
    async def generate(self, prompt: str, *args, **kwargs) -> str:
        """
        Generate an answer to the given prompt.
        """
        raise NotImplementedError
