import pytest

from addressr_client.client import AddressrClient


@pytest.mark.asyncio
async def test_client():
    client = AddressrClient(
        base_url="http://localhost:5001"
    )

    response = await client.address.search("4 Batten Crescent")

    assert response is not None