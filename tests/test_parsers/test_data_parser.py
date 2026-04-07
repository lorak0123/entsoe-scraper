import pytest

from entsoe_api.enums import DocumentType
from entsoe_api.parser.data_parser import DataParser


def test_data_parser_to_dataframe(resource_xml_data: bytes | None, resource_params_document_type: DocumentType | None):
    """Test that the DataParser can convert parsed data to a DataFrame."""
    if resource_xml_data is not None and resource_params_document_type is not None:
        res = DataParser.parse_to_dataframe(resource_xml_data, resource_params_document_type)
        assert res is not None, "Parsed DataFrame should not be None."
        assert not res.empty, "Parsed DataFrame should not be empty."
    else:
        pytest.skip("No XML data or document type provided for this resource.")


def test_data_parser_to_dataframe_set(
    resource_xml_data: bytes | None, resource_params_document_type: DocumentType | None
):
    """Test that the DataParser can convert parsed data to a set of DataFrames."""
    if resource_xml_data is not None and resource_params_document_type is not None:
        res = DataParser.parse_data_to_dataframe_set(resource_xml_data, resource_params_document_type)
        assert res is not None, "Parsed DataFrame set should not be None."
        assert isinstance(res, dict), "Parsed data should be a dictionary of DataFrames."
        assert len(res) > 0, "Parsed DataFrame set should contain at least one DataFrame."
    else:
        pytest.skip("No XML data or document type provided for this resource.")
