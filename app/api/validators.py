from fastapi import HTTPException

from app.core.exceptions import (
    InvalidAddressError,
    AddressNotFoundError,
    TronNetworkError
)
from app.tronpy.client import TronClient


async def check_tron_address_exists(
        address: str,
        tron_client: TronClient
) -> dict:
    """Check if tron address correct and exists > return."""
    try:
        info = await tron_client.get_info_by_address(address)
        return info
    except InvalidAddressError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except AddressNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except TronNetworkError as e:
        raise HTTPException(status_code=503, detail=str(e))
