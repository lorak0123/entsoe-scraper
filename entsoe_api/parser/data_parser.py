import pandas as pd

from entsoe_api.enums import DocumentType
from entsoe_api.parser.parser_extensions.price_data_parser import PriceDataParser
from entsoe_api.parser.parser_extensions.production_data_parser import ProductionDataParser
from entsoe_api.parser.parser_interface import ParserInterface
from entsoe_api.parser.exceptions import ParserError


class DataParser:
    """A class for parsing various types of XML data into pandas DataFrame."""

    def __init__(self):
        self.parsers: dict[DocumentType, type[ParserInterface]] = {
            DocumentType.ACTUAL_GENERATION_PER_TYPE: ProductionDataParser,
            DocumentType.PRICE_DOCUMENT: PriceDataParser,
        }

    def parse_data(self, xml_data: bytes, document_type: DocumentType) -> pd.DataFrame:
        """
        Main method to parse the XML data based on document type.

        Args:
            xml_data (bytes): The XML data to parse.
            document_type (DocumentType): The type of document to parse.

        Returns:
            pd.DataFrame: Parsed data in DataFrame format.
        """
        if document_type not in self.parsers:
            raise ParserError(f"Parser for document type '{document_type}' is not defined.")

        # Get the specific parser for the document type
        return self.parsers[document_type].parse(xml_data)
