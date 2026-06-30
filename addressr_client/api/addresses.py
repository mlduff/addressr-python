import httpx
from pydantic import TypeAdapter

from addressr_client.schemas.search_addresses import AddressSearchResponse
from addressr_client.schemas.get_address import AddressGetResponse

address_response_adapter = TypeAdapter(AddressSearchResponse)

class AddressApi():

    def __init__(self, client: httpx.AsyncClient):
        self.client = client

    async def search(self, query: str) -> AddressSearchResponse:
        response = await self.client.get(
            "/addresses",
            params={
                "q": query
            }
        )

        return address_response_adapter.validate_python(response.json())
    
    async def get(self, pid: str) -> AddressGetResponse:
        response = await self.client.get(
            f"/addresses/{pid}"
        )

        return AddressGetResponse.model_dump_json(response.json())