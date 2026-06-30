import httpx

from addressr_client.api.addresses import AddressApi

async def raise_on_4xx_5xx(response):
    response.raise_for_status()

class AddressrClient():

    def __init__(self, base_url: str, api_key: str=None):
        self._base_url = base_url
        self._api_key = api_key

        headers = {}
        if api_key is not None:
            headers["x-rapidapi-key"] = self._api_key

        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            event_hooks={
                "response": [raise_on_4xx_5xx],
            },
            headers=headers,
        )

        self.address = AddressApi(
            self._client
        )

    async def close(self):
        await self._client.aclose()

