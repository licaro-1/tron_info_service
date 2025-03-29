from typing import TypeVar, Sequence

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import Base
from app.schemas.tron_request import TronRequestCreate
from app.models.tron_request import TronRequest


ModelType = TypeVar("ModelType", bound=Base)


class CRUDTronRequest:
    def __init__(self, model: ModelType):
        self.model = model

    async def create(
            self,
            session: AsyncSession,
            obj_in: TronRequestCreate
    ) -> ModelType:
        obj_in_dict = obj_in.model_dump()
        db_obj = self.model(**obj_in_dict)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_multi(
            self,
            session: AsyncSession,
            limit: int = 10,
            offset: int = 0
    ) -> Sequence[TronRequest]:
        stmt = (
            select(self.model)
            .order_by(desc(self.model.requested_at))
            .limit(limit)
            .offset(offset)
        )
        db_objs = await session.execute(stmt)
        return db_objs.scalars().all()


tron_request_crud = CRUDTronRequest(TronRequest)
