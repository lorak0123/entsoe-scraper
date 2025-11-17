# Project structure

A short description of the project's top-level layout and important files.

- `entsoe_api/` — package source code
  - `api.py` — ENTSO-E client (`EntsoeAPI`)
  - `parser/` — XML parsers → pandas.DataFrame
  - `enums/` — enum definitions (`DocumentType`, `DomainType`, etc.)
  - `scripts/` — CLI tools (e.g. `entsoe_fetcher.py`)
  - `utils.py` — logger and helper utilities
- `docs/` — project documentation (this folder)
- `data/` — sample and generated CSV/HTML files
- `build/` — build artifacts

Config files

- `pyproject.toml` — package and dependency configuration
- `README.md` — main project README and usage examples
- `CHANGELOG.md` — project changelog

See [Documentation index](index.md) for links to each section.

---

Navigation

- [Back to Index](index.md)
- [For developers](development.md)
- [CLI guide](cli.md)
