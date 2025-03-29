from datetime import datetime
from typing import Sequence, Any

from pydantic import BaseModel, Field, field_validator


class TronRequestBase(BaseModel):
    address: str = Field(..., min_length=34)

    @field_validator("address")
    def validate_address(cls, value):
        if not value.startswith("T") or len(value) != 34:
            raise ValueError(
                "Address must start with 'T' and be 34 characters long."
            )
        return value

    class Config:
        from_attributes = True


class TronRequestDto(TronRequestBase):
    pass


class TronRequestCreate(TronRequestBase):
    bandwidth: int
    energy: int
    trx_balance: float


class TronRequestDB(TronRequestCreate):
    bandwidth: int
    energy: int
    requested_at: datetime
    trx_balance: float


class TronRequestPagintaion(BaseModel):
    items: Sequence[TronRequestDB]
    limit: int
    offset: int
