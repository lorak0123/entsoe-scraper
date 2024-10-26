# Changelog

All notable changes to this project will be documented in this file.

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
