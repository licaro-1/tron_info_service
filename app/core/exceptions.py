class TronClientError(Exception):
    """Base exception class for Tron client."""


class InvalidAddressError(TronClientError):
    """Error: Invalid address."""


class AddressNotFoundError(TronClientError):
    """Error: Address not found."""


class TronNetworkError(TronClientError):
    """Error: Problems with network."""
