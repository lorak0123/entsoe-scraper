"""Parser for price data XML returned by the ENTSO-E API."""

from entsoe_api.parser.parser_interface import ParserInterface


class PriceDataParser(ParserInterface):
    """A parser for price data XML returned by the ENTSO-E API."""

    POINT_VALUE_TAG = "price.amount"

    @classmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Extract the name of the time series from the XML element."""
        sequence = time_series_element.find("ns:classificationSequence_AttributeInstanceComponent.position", namespace)
        if sequence is not None:
            return f"PRICE_SEQUENCE_{sequence.text}"
        return "PRICE"

    @classmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        return {
            "unit": f"{time_series_element.find('ns:currency_Unit.name', namespace).text}/{
                time_series_element.find('ns:price_Measure_Unit.name', namespace).text
            }",
        }
