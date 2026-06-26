from httpx import AsyncClient, Response, AsyncHTTPTransport


class BaseHttpClient:
    async def get(
            self,
            url: str,
            params: dict,
            *args,
            retries: int = 3,
            timeout: int = 60,
            **kwargs,
    ) -> Response:
        """
        Send GET request to given URL.
        """
        transport = AsyncHTTPTransport(retries=retries)

        async with AsyncClient(transport=transport, timeout=timeout) as client:
            response = await client.get(
                *args,
                url=url,
                params=params,
                **kwargs,
            )
            return response

    async def post(self, url: str, *args, timeout: int = 60, **kwargs) -> Response:
        """
        Send POST request to given URL.
        """
        async with AsyncClient(verify=False, timeout=timeout) as client:
            response = await client.post(
                *args,
                url=url,
                **kwargs,
            )
            return response