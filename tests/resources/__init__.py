from datetime import datetime

from entsoe_api.enums import DocumentType, DomainType, ProcessType

RESOURCES_CONFIG = [
    {
        "path": "tests/resources/sample_data.xml",
        "params": dict(
            start_date=datetime(2025, 1, 1),
            end_date=datetime(2025, 12, 31),
            document_type=DocumentType.WIND_AND_SOLAR_FORECAST,
            process_type=ProcessType.DAY_AHEAD,
            in_domain=DomainType.NO2,
        ),
    }
]
