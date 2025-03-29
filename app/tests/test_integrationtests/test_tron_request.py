import pytest


@pytest.mark.asyncio
async def test_get_tron_info(ac):
    response = await ac.post(
        "/",
        json={
            "address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g"
        }
    )
    assert response.status_code == 200
    address_data = response.json()
    assert "address" in address_data
    assert "bandwidth" in address_data
    assert "energy" in address_data
    assert "trx_balance" in address_data
    assert "requested_at" in address_data

    # GET response for all requests
    response = await ac.get("/")
    assert response.status_code == 200
    requests_data = response.json()
    items, limit, offset = (requests_data["items"],
                            requests_data["limit"],
                            requests_data["offset"])
    assert isinstance(items, list)
    assert len(items) > 0
    assert limit == 10
    assert offset == 0
    assert items[0] == address_data
