"""Installed Capacity data parser for XML returned by the ENTSO-E API."""

from entsoe_api.enums import PsrType
from entsoe_api.parser.parser_interface import ParserInterface


class InstalledCapacityDataParser(ParserInterface):
    """A parser for installed capacity data XML returned by the ENTSO-E API."""

    @classmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Extract the name of the time series from the XML element."""
        return PsrType(time_series_element.find(".//ns:psrType", namespace).text).name + "_INSTALLED_CAPACITY"

    @classmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        return {
            "unit": time_series_element.find("ns:quantity_Measure_Unit.name", namespace).text,
        }
