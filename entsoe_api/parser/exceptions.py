from entsoe_api.exceptions import EntsoeApiError


class ParserError(EntsoeApiError):
    """Raised when an error occurs while parsing data"""
