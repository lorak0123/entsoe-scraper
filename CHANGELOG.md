# Changelog

All notable changes to this project will be documented in this file.

---

## [1.1.0] - 2025-11-17

### Changed

- Refactored `entsoe_api.api.EntsoeAPI`: added configurable `max_period_days` parameter; renamed `domain` parameter to `in_domain` and `out_domain`; added `OutBiddingZone_Domain` request parameter; improved chunking logic to use `max_period_days` and corrected chunk end handling for price documents; improved request logging; removed an unused XML import.
- Updated `entsoe_api.enums.code_bindings.domain_type.DomainType`: corrected the DE code and expanded the enum with many additional domain/area codes.
- CLI (`entsoe_api.scripts.entsoe_fetcher`): replaced `--domain` with `--in-domain` and added `--out-domain`; changed output flag handling (output is now optional and `--output` short flag changed to `-f`); added `--chunk_size` option; the CLI now passes chunk size to `EntsoeAPI`.
- Parser bugfixes: fixed off-by-one timestamp calculation in `entsoe_api/parser/parser_extensions/price_data_parser.py` and `production_data_parser.py`.
- Logging: `entsoe_api.utils` now adds a `StreamHandler` to the project logger to enable console output.

### Added

- Registered new parsers in `entsoe_api.parser.data_parser`: `AGGREGATED_ENERGY_DATA_REPORT`, `WIND_AND_SOLAR_FORECAST`, and `SYSTEM_TOTAL_LOAD`.
- Added imports for `AggregatedEnergyDataDataParser` and `TotalLoad` parser classes.

---

## [1.0.0] - 2024-10-26

### Added

- Implemented the **EntsoeAPI** core class for interacting with the ENTSO-E Transparency Platform API.
- Added support for **data fetching** with various parameters, including:
    - Document type
    - Process type
    - Market domain
    - PSR type (generation source)
- Implemented **data chunking** for large date ranges to avoid exceeding API limits.
- Integrated **interval parsing** from XML `<resolution>` tag to automatically detect data intervals.
- Included initial CLI tool: `entsoe-fetcher`, allowing:
    - Setting start and end dates
    - Specifying document, process, and market domain
    - Saving data to CSV format
- Set up flexible and extensible **DataParser** structure for handling different document types.
- Initial version of **documentation** in `docs/` directory with:
    - Usage examples
    - API reference
    - Developer setup instructions

---

## [Upcoming Features]

### Planned

- Additional parsers for more document types (e.g., forecast, outage data).
- Unit tests for core functions and parsers.
- Improved error handling and retry mechanism for API requests.
- Enhanced CLI with additional flags for data format options.

---

### Notes

- This release includes initial documentation in the `docs/` directory, detailing installation, usage, and API
  structure.
- For quickstart guidance, see `README.md`.

---
