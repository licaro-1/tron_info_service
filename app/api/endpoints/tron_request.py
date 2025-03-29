from fastapi import APIRouter, Depends, Query

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import tron_request
from app.core.db import get_async_session
from app.tronpy.client import tron_client
from app.crud.tron_request import tron_request_crud
from app.api.validators import check_tron_address_exists


router = APIRouter()


@router.post(
    "/",
    response_model=tron_request.TronRequestDB
)
async def get_tron_info(
        address: tron_request.TronRequestDto,
        session: AsyncSession = Depends(get_async_session)
):

    tron_info = await check_tron_address_exists(
        address.address,
        tron_client
    )
    obj_in = tron_request.TronRequestCreate(
        **tron_info
    )
    db_obj = await tron_request_crud.create(
        session=session,
        obj_in=obj_in
    )
    return db_obj


@router.get(
    "/",
    response_model=tron_request.TronRequestPagintaion
)
async def get_all_tron_requests(
    limit: int = Query(
        10, ge=1, le=100, description="Objects count on page"
    ),
    offset: int = Query(0, ge=0, description="Offset"),
    session: AsyncSession = Depends(get_async_session)
):
    db_objects = await tron_request_crud.get_multi(
        session=session,
        limit=limit,
        offset=offset
    )
    result = {
        "items": [
            tron_request.TronRequestDB.model_validate(obj)
            for obj in db_objects
        ],
        "limit": limit,
        "offset": offset
    }
    return tron_request.TronRequestPagintaion(**result)
