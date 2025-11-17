# API — module and class descriptions

This section describes the main classes and modules provided by the project.

EntsoeAPI (entsoe_api.api.EntsoeAPI)

- Purpose: the primary client for fetching data from the ENTSO-E Transparency Platform.
- Constructor: `EntsoeAPI(api_key: str, max_period_days: int = 30)` — allows configuring the maximum period (in days) per single request.
- Key methods:
  - `_get_data(start_date, end_date, document_type, process_type, in_domain, out_domain, psr_type)` — low-level method that fetches raw XML from the API.
  - `fetch_data(start_date, end_date, document_type, process_type, in_domain, out_domain=None, psr_type='ALL') -> pd.DataFrame` — high-level method that returns a pandas.DataFrame with parsed data.
- Notes:
  - `max_period_days` is used to split long date ranges into smaller chunks to comply with API limits.
  - `in_domain` and `out_domain` specify the bidding zone or area codes (see `entsoe_api.enums.code_bindings.domain_type.DomainType`).

DataParser (entsoe_api.parser.data_parser.DataParser)

- Responsible for delegating XML payloads to the appropriate extension parsers.
- Registered parsers (examples):
  - `ACTUAL_GENERATION_PER_TYPE` → `ProductionDataParser`
  - `PRICE_DOCUMENT` → `PriceDataParser`
  - `AGGREGATED_ENERGY_DATA_REPORT` → `AggregatedEnergyDataDataParser`
  - `WIND_AND_SOLAR_FORECAST` → `ProductionDataParser`
  - `SYSTEM_TOTAL_LOAD` → `TotalLoad`

Parser extensions (entsoe_api/parser/parser_extensions)

- Each parser implements `ParserInterface` and returns a `pandas.DataFrame`.
- Notable fixes/changes:
  - Corrected timestamp (offset) calculation in `PriceDataParser` and `ProductionDataParser`.

Enums (entsoe_api.enums)

- `DomainType` contains ENTSO-E bidding zone/area codes (BZN) — the enum was extended with multiple codes and the DE entry was corrected.
- `DocumentType`, `ProcessType`, `PsrType` — provide standard values used in API requests.

Logger

- `entsoe_api.utils.LOGGER` is configured at package level and includes a default `StreamHandler` for console output.

See the [CLI](cli.md) for examples of invoking the API from the terminal and [Usage](usage.md) for quickstart examples.

---

Navigation

- [Back to Index](index.md)
- [Usage (Quickstart)](usage.md)
- [CLI guide](cli.md)
