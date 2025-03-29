from sqlalchemy import Column, String, Integer, DateTime, func, Float

from app.core.db import Base


class TronRequest(Base):
    __tablename__ = "tron_request"
    address = Column(String, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    trx_balance = Column(Float, nullable=False)
    requested_at = Column(
        DateTime,
        default=func.now(),
        nullable=False
    )
