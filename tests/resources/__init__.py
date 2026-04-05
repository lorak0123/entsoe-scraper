from datetime import datetime

from entsoe_api.enums import DocumentType, DomainType, ProcessType

RESOURCES_CONFIG = [
    {
        "path": "xml_resources/wind_and_solar_forecast_no2_2025.xml",
        "params": dict(
            start_date=datetime(2025, 1, 1),
            end_date=datetime(2025, 12, 31),
            document_type=DocumentType.WIND_AND_SOLAR_FORECAST,
            process_type=ProcessType.DAY_AHEAD,
            in_domain=DomainType.NO2,
        ),
        "expected_columns": ["SOLAR", "WIND_OFFSHORE", "WIND_ONSHORE"],
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2025, 1, 1, 0, 0),
        "expected_end_timestamp": datetime(2025, 12, 31, 23, 0),
        "excepted_errors": None,
    },
    {
        "path": "xml_resources/wind_and_solar_forecast_de_lu_2022-01.xml",
        "params": dict(
            start_date=datetime(2022, 1, 1),
            end_date=datetime(2022, 1, 31),
            document_type=DocumentType.WIND_AND_SOLAR_FORECAST,
            process_type=ProcessType.DAY_AHEAD,
            in_domain=DomainType.DE_LU,
        ),
        "expected_columns": ["SOLAR", "WIND_OFFSHORE", "WIND_ONSHORE"],
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2022, 1, 1, 0, 0),
        "expected_end_timestamp": datetime(2022, 1, 31, 23, 0),
        "excepted_errors": None,
    },
    {
        "path": "xml_resources/actual_generation_per_type_pl_2026-04-04.xml",
        "params": dict(
            start_date=datetime(2026, 4, 4),
            end_date=datetime(2026, 4, 5),
            document_type=DocumentType.ACTUAL_GENERATION_PER_TYPE,
            process_type=ProcessType.REALISED,
            in_domain=DomainType.PL,
        ),
        "expected_columns": [
            "BIOMASS",
            "FOSSIL_BROWN_COAL_LIGNITE",
            "FOSSIL_COAL_DERIVED_GAS",
            "FOSSIL_GAS",
            "FOSSIL_HARD_COAL",
            "FOSSIL_OIL",
            "HYDRO_PUMPED_STORAGE",
            "HYDRO_RUN_OF_RIVER_POUNDAGE",
            "HYDRO_WATER_RESERVOIR",
            "OTHER",
            "OTHER_RENEWABLE",
            "SOLAR",
            "WIND_ONSHORE",
        ],
        "expected_rows": 96,  # max position from xml
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2026, 4, 4, 0, 0),
        "expected_end_timestamp": datetime(2026, 4, 5, 0, 0),
        "excepted_errors": None,
    },
    {
        "path": "xml_resources/price_document_fr_2016-05-13.xml",
        "params": dict(
            start_date=datetime(2016, 5, 12, 22),
            end_date=datetime(2016, 5, 13, 22),
            document_type=DocumentType.PRICE_DOCUMENT,
            process_type=ProcessType.REALISED,
            in_domain=DomainType.FR,
        ),
        "expected_rows": 24,  # max position from xml
        "expected_columns": ["Price"],
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2016, 5, 12, 22, 0),
        "expected_end_timestamp": datetime(2016, 5, 13, 22, 0),
        "excepted_errors": None,
    },
    {
        "path": "xml_resources/system_total_load_es_2024-08-19.xml",
        "params": dict(
            start_date=datetime(2024, 8, 18, 22),
            end_date=datetime(2024, 8, 19, 22),
            document_type=DocumentType.SYSTEM_TOTAL_LOAD,
            process_type=ProcessType.DAY_AHEAD,
            in_domain=DomainType.ES,
        ),
        "expected_rows": 96,  # max position from xml
        "expected_columns": ["unit", "resolution", "Quantity"],
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2024, 8, 18, 22, 0),
        "expected_end_timestamp": datetime(2024, 8, 19, 22, 0),
        "excepted_errors": None,
    },
    {
        "path": "xml_resources/aggregated_energy_es-fr_2024-08-19.xml",
        "params": dict(
            start_date=datetime(2024, 8, 18, 22),
            end_date=datetime(2024, 8, 19, 22),
            document_type=DocumentType.AGGREGATED_ENERGY_DATA_REPORT,
            process_type=ProcessType.REALISED,
            in_domain=DomainType.ES,
            out_domain=DomainType.FR,
        ),
        "expected_rows": 96,  # max position from xml
        "expected_columns": ["unit", "resolution", "Quantity"],
        "expected_index_name": "timestamp",
        "expected_start_timestamp": datetime(2024, 8, 18, 22, 0),
        "expected_end_timestamp": datetime(2024, 8, 19, 22, 0),
        "excepted_errors": None,
    },
]
