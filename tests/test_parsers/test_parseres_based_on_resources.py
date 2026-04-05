from datetime import datetime

import pytest

from entsoe_api.enums import DocumentType
from entsoe_api.parser.data_parser import DataParser


def test_if_parsers_parse_resources_with_no_errors(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_error: Exception | None,
):
    """Test that the parsers can parse the XML resources without errors."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_error is None:
        data_parser = DataParser()
        try:
            parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
            assert parsed_data is not None, "Parsed data should not be None."
        except Exception as e:
            pytest.fail(f"Parsing failed with an exception: {e}")
    else:
        pytest.skip("No XML data or document type provided for this resource, or expected errors are defined.")


def test_if_parsed_data_does_not_exits_start_timestamp(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_start_timestamp: datetime | None,
):
    """Test that the parsed data does not contain timestamps before the expected start timestamp."""
    if (
        resource_xml_data is not None
        and resource_params_document_type is not None
        and expected_start_timestamp is not None
    ):
        data_parser = DataParser()
        try:
            parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
            assert parsed_data.index.min() >= expected_start_timestamp, (
                "Parsed data contains timestamps before the expected start timestamp."
            )
        except Exception as e:
            pytest.fail(f"Parsing failed with an exception: {e}")
    else:
        pytest.skip("No XML data, document type, or expected start timestamp provided for this resource.")


def test_if_parsed_data_does_not_exits_end_timestamp(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_end_timestamp: datetime | None,
):
    """Test that the parsed data does not contain timestamps after the expected end timestamp."""
    if (
        resource_xml_data is not None
        and resource_params_document_type is not None
        and expected_end_timestamp is not None
    ):
        data_parser = DataParser()
        try:
            parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
            assert parsed_data.index.max() <= expected_end_timestamp, (
                "Parsed data contains timestamps after the expected end timestamp."
            )
        except Exception as e:
            pytest.fail(f"Parsing failed with an exception: {e}")
    else:
        pytest.skip("No XML data, document type, or expected end timestamp provided for this resource.")


def test_if_parsed_data_contains_expected_columns(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_columns: list[str] | None,
):
    """Test that the parsed data contains the expected columns."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_columns is not None:
        data_parser = DataParser()
        parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
        assert all(column in parsed_data.columns for column in expected_columns), (
            "Parsed data does not contain all expected columns."
        )
    else:
        pytest.skip("No XML data, document type, or expected columns provided for this resource.")


def test_if_parsed_data_has_expected_index_name(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_index_name: str | None,
):
    """Test that the parsed data has the expected index name."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_index_name is not None:
        data_parser = DataParser()
        try:
            parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
            assert parsed_data.index.name == expected_index_name, (
                f"Parsed data index name '{parsed_data.index.name}' does not match "
                f"expected index name '{expected_index_name}'."
            )
        except Exception as e:
            pytest.fail(f"Parsing failed with an exception: {e}")
    else:
        pytest.skip("No XML data, document type, or expected index name provided for this resource.")


def test_if_parsed_data_has_expected_number_of_rows(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_rows: int | None,
):
    """Test that the parsed data has the expected number of rows."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_rows is not None:
        data_parser = DataParser()
        try:
            parsed_data = data_parser.parse_data(resource_xml_data, resource_params_document_type)
            assert len(parsed_data) == expected_rows, (
                f"Parsed data has {len(parsed_data)} rows, but expected {expected_rows} rows."
            )
        except Exception as e:
            pytest.fail(f"Parsing failed with an exception: {e}")
    else:
        pytest.skip("No XML data, document type, or expected number of rows provided for this resource.")


def test_if_parsers_raise_expected_errors(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_error: Exception | None,
):
    """Test that the parsers raise the expected errors when parsing the XML resources."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_error is not None:
        data_parser = DataParser()
        with pytest.raises(type(expected_error)) as exc_info:
            data_parser.parse_data(resource_xml_data, resource_params_document_type)
        assert str(exc_info.value) == str(expected_error), (
            f"Expected error message '{expected_error}', but got '{exc_info.value}'."
        )
    else:
        pytest.skip("No XML data, document type, or expected error provided for this resource.")
