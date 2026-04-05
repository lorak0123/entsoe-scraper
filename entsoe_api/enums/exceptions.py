"""Module with custom exceptions for the entsoe_api package."""

from entsoe_api.exceptions import EntsoeApiError


class CodeBindingError(EntsoeApiError):
    """Raised when a code binding error occurs."""
