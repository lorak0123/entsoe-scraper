"""Parser for total load data from the ENTSO-E API."""

from entsoe_api.parser.parser_interface import ParserInterface


class TotalLoad(ParserInterface):
    """Parser for total load data from the ENTSO-E API.

    This parser processes XML data related to total load, extracting relevant information such as timestamps,
    quantities, and units. The parsed data is returned as a pandas DataFrame for further analysis and manipulation.
    """

    @classmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Return a fixed name for the total load time series."""
        return "TOTAL_LOAD"

    @classmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        return {"unit": time_series_element.find("ns:quantity_Measure_Unit.name", namespace).text}
