from httpx import AsyncClient, Response


class BaseHttpClient:
    async def get(self, url: str, params: dict, *args, **kwargs) -> Response:
        """
        Send GET request to given URL.
        """
        async with AsyncClient() as client:
            response = await client.get(
                *args,
                url=url,
                params=params,
                **kwargs,
            )
            return response

    async def post(self, url: str, *args, **kwargs) -> Response:
        """
        Send POST request to given URL.
        """
        async with AsyncClient(verify=False, timeout=60) as client:
            response = await client.post(
                *args,
                url=url,
                **kwargs,
            )
            return response
