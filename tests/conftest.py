from datetime import datetime
from pathlib import Path
from typing import Any

import pytest

from entsoe_api.enums import DocumentType, DomainType, ProcessType, PsrType
from tests.resources import RESOURCES_CONFIG


@pytest.fixture(params=RESOURCES_CONFIG, ids=lambda c: c["path"])
def resource_config(request) -> dict:
    """Fixture to provide resource configurations for tests."""
    return request.param


@pytest.fixture
def resource_path(resource_config) -> Path | None:
    """Fixture to provide the path to the XML resource file."""
    res_path = resource_config.get("path")
    if res_path is not None:
        return Path(__file__).parent / "resources" / res_path
    return None


@pytest.fixture
def resource_xml_data(resource_path) -> bytes | None:
    """Fixture to read the XML data from the resource file."""
    if resource_path is not None:
        with open(resource_path, encoding="utf-8") as file:
            return file.read().encode("utf-8")
    return None


# The following fixtures extract specific parameters from the resource configuration for use in tests.


@pytest.fixture
def resource_params(resource_config) -> dict[str, Any] | None:
    """Fixture to provide the parameters for parsing the XML resource."""
    return resource_config.get("params")


@pytest.fixture
def resource_params_start_timestamp(resource_params) -> datetime | None:
    """Fixture to provide the expected start timestamp for the resource."""
    if resource_params:
        return resource_params.get("start_date")
    return None


@pytest.fixture
def resource_params_end_timestamp(resource_params) -> datetime | None:
    """Fixture to provide the expected end timestamp for the resource."""
    if resource_params:
        return resource_params.get("end_date")
    return None


@pytest.fixture
def resource_params_document_type(resource_params) -> DocumentType | None:
    """Fixture to provide the expected document type for the resource."""
    if resource_params:
        return resource_params.get("document_type")
    return None


@pytest.fixture
def resource_params_process_type(resource_params) -> ProcessType | None:
    """Fixture to provide the expected process type for the resource."""
    if resource_params:
        return resource_params.get("process_type")
    return None


@pytest.fixture
def resource_params_in_domain(resource_params) -> DomainType | None:
    """Fixture to provide the expected in domain for the resource."""
    if resource_params:
        return resource_params.get("in_domain")
    return None


@pytest.fixture
def resource_params_out_domain(resource_params) -> DomainType | None:
    """Fixture to provide the expected out domain for the resource."""
    if resource_params:
        return resource_params.get("out_domain")
    return None


@pytest.fixture
def resource_params_psr_type(resource_params) -> PsrType | None:
    """Fixture to provide the expected PSR type for the resource."""
    if resource_params:
        return resource_params.get("psr_type")
    return None


# The following fixtures extract expected values from the resource configuration for use in assertions in tests.


@pytest.fixture
def expected_columns(resource_config) -> list[str] | None:
    """Fixture to provide the expected columns for the resource."""
    return resource_config.get("expected_columns")


@pytest.fixture
def expected_rows(resource_config) -> dict[str, int] | None:
    """Fixture to provide the expected number of rows for the resource."""
    return resource_config.get("expected_rows")


@pytest.fixture
def expected_start_timestamp(resource_config) -> datetime | None:
    """Fixture to provide the expected start timestamp for the resource."""
    return resource_config.get("expected_start_timestamp")


@pytest.fixture
def expected_end_timestamp(resource_config) -> datetime | None:
    """Fixture to provide the expected end timestamp for the resource."""
    return resource_config.get("expected_end_timestamp")


@pytest.fixture
def expected_error(resource_config) -> Exception | None:
    """Fixture to provide the expected errors for the resource."""
    return resource_config.get("excepted_errors")
