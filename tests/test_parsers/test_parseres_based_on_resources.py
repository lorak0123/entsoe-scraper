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
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)

        assert parsed_data is not None, "Parsed data should not be None."
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
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)

        for time_series in parsed_data:
            for timestamp, _ in time_series.data:
                assert timestamp >= expected_start_timestamp, (
                    "Parsed data contains timestamps before the expected start timestamp."
                )
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
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)

        for time_series in parsed_data:
            for timestamp, _ in time_series.data:
                assert timestamp <= expected_end_timestamp, (
                    "Parsed data contains timestamps after the expected end timestamp."
                )
    else:
        pytest.skip("No XML data, document type, or expected end timestamp provided for this resource.")


def test_if_parsed_data_contains_expected_columns(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_columns: list[str] | None,
):
    """Test that the parsed data contains the expected columns."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_columns is not None:
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)
        for time_series in parsed_data:
            assert time_series.name in expected_columns, (
                f"Parsed data contains time series '{time_series.name}' "
                f"which is not in the expected columns {expected_columns}."
            )
    else:
        pytest.skip("No XML data, document type, or expected columns provided for this resource.")


def test_if_parsed_data_has_proper_types(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
):
    """Test that the parsed data has the proper types."""
    if resource_xml_data is not None and resource_params_document_type is not None:
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)
        for time_series in parsed_data:
            assert isinstance(time_series.name, str), "Time series name should be a string."
            for timestamp, value in time_series.data:
                assert isinstance(timestamp, datetime), "Timestamp should be a datetime object."
                assert isinstance(value, (int, float)), "Value should be an integer or float."
    else:
        pytest.skip("No XML data or document type provided for this resource.")


def test_if_parsed_data_has_expected_number_of_rows(
    resource_xml_data: bytes | None,
    resource_params_document_type: DocumentType | None,
    expected_rows: int | None,
):
    """Test that the parsed data has the expected number of rows."""
    if resource_xml_data is not None and resource_params_document_type is not None and expected_rows is not None:
        parsed_data = DataParser.PARSERS[resource_params_document_type].parse(resource_xml_data)
        name_to_time_series = {time_series.name: time_series for time_series in parsed_data}
        for column_name, expected_row_count in expected_rows.items():
            assert column_name in name_to_time_series, f"Expected column '{column_name}' not found in parsed data."
            actual_row_count = len(name_to_time_series[column_name].data)
            assert actual_row_count == expected_row_count, (
                f"Expected {expected_row_count} rows for column '{column_name}', but got {actual_row_count}."
            )
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
