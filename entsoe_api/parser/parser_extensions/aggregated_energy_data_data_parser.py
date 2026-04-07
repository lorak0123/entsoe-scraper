"""Parser for aggregated energy data XML returned by the ENTSO-E API."""

from entsoe_api.enums import DomainType
from entsoe_api.parser.parser_interface import ParserInterface


class AggregatedEnergyDataDataParser(ParserInterface):
    """A parser for aggregated energy data XML returned by the ENTSO-E API."""

    @classmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Extract the name of the time series from the XML element."""
        sender = DomainType(time_series_element.find("ns:out_Domain.mRID", namespace).text).name
        receiver = DomainType(time_series_element.find("ns:in_Domain.mRID", namespace).text).name

        return f"FLOW_{sender}_TO_{receiver}"

    @classmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        return {"unit": time_series_element.find("ns:quantity_Measure_Unit.name", namespace).text}
