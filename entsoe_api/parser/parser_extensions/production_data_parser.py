"""Production data parser for XML returned by the ENTSO-E API."""

from entsoe_api.enums import PsrType
from entsoe_api.parser.parser_interface import ParserInterface


class ProductionDataParser(ParserInterface):
    """A parser for production data XML returned by the ENTSO-E API."""

    @classmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Extract the name of the time series from the XML element."""
        if time_series_element.find(".//ns:outBiddingZone_Domain.mRID", namespace) is not None:
            return PsrType(time_series_element.find(".//ns:psrType", namespace).text).name + "_CONSUMPTION"
        else:
            return PsrType(time_series_element.find(".//ns:psrType", namespace).text).name + "_GENERATION"

    @classmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        return {
            "unit": time_series_element.find("ns:quantity_Measure_Unit.name", namespace).text,
        }
