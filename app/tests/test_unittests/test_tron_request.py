import pytest

from app.schemas.tron_request import TronRequestCreate
from app.models.tron_request import TronRequest
from app.crud.tron_request import CRUDTronRequest


@pytest.mark.asyncio
async def test_create_tron_request(db_session):
    tron_data = {
        "bandwidth": 1000,
        "energy": 50,
        "address": "TZ4UXDV5ZhNW7fb2AMSbgfAEZ7hWsnYS2g",
        "trx_balance": 70.25
    }
    obj_in = TronRequestCreate(**tron_data)
    crud_tron_request = CRUDTronRequest(TronRequest)
    db_obj = await crud_tron_request.create(db_session, obj_in)
    assert db_obj is not None
    assert db_obj.bandwidth == tron_data["bandwidth"]
    assert db_obj.energy == tron_data["energy"]
    assert db_obj.address == tron_data["address"]
    assert db_obj.trx_balance == tron_data["trx_balance"]
    assert db_obj.id is not None
