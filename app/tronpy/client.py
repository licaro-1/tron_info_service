from typing import Union

from tronpy.async_tron import AsyncTron
from tronpy.providers.async_http import AsyncHTTPProvider
from tronpy.exceptions import (
    AddressNotFound,
    BadAddress,
    UnknownError
)
from app.core.config import settings
from app.core import exceptions as custom_tron_exc


class TronClient:
    def __init__(self, network: str, provider):
        """
        Initialize tron client with network and provider.
        """
        self.client = AsyncTron(
            network=network,
            provider=provider
        )

    async def get_info_by_address(
            self,
            address: str
    ) -> dict[str, Union[str, int]] | None:
        """
        Get info about Tron wallet.
        :return: Dictionary with bandwidth and energy
        """
        try:
            resource_info = await self.client.get_account_resource(address)
            bandwidth = resource_info.get("freeNetLimit", 0)
            energy = resource_info.get("EnergyLimit", 0)
            account_info = await self.client.get_account(address)
            trx_balance = account_info.get("balance", 0) / 1_000_000
            return {
                "bandwidth": bandwidth,
                "energy": energy,
                "address": address,
                "trx_balance": trx_balance
            }
        except BadAddress:
            raise custom_tron_exc.InvalidAddressError(
                "Invalid Tron address format."
            )
        except AddressNotFound:
            raise custom_tron_exc.AddressNotFoundError(
                "Tron address not found."
            )
        except UnknownError:
            raise custom_tron_exc.TronNetworkError(
                "Error connecting to Tron network."
            )


tron_client = TronClient(
    network="mainnet",
    provider=AsyncHTTPProvider(api_key=settings.TRON_API_KEY)
)
