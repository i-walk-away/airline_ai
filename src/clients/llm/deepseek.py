import json

from src.clients.llm.abstract import AbstractLlmClient
from config.config import settings


class DeepSeekClient(AbstractLlmClient):
    URL = "https://openrouter.ai/api/v1/chat/completions"
    MODEL = "tngtech/deepseek-r1t2-chimera:free"

    async def generate(self, prompt: str, *args, **kwargs) -> str:
        headers = {
            "Authorization": f"Bearer {settings.open_router.api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": self.MODEL,
            "messages": [
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            "extra_body": {"reasoning": {"enabled": False}}
        }

        response = await self.http_service.post(
            self.URL,
            headers=headers,
            data=json.dumps(data),
        )
        try:
            result = response.json().get("choices")[0].get("message").get("content")
        except (KeyError, TypeError) as exc:
            result = "Failed to generate an answer. Try again later"
            # Proper logging could be implemented later
            print(f"Failed to generate an answer for prompt '{prompt}': {exc}")

        return result