# For Developers

This section is for contributors who want to develop the project locally.

Quick environment setup

1. Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate  # Windows PowerShell
```

2. Install the package in editable mode:

```bash
pip install -e .
```

3. (Recommended for development) Install development dependencies:

```powershell
pip install -e .[dev]
```

Running tests and linters

- Tests: run `pytest` from the project root. See the "Running tests and coverage" section below for coverage options.
- Linting: we use `ruff`, `isort` and `pre-commit` (configuration in `pyproject.toml`).

Style and conventions

- Type hints: the project targets Python 3.8+ and uses type annotations. Prefer explicit types in public APIs.
- New features: add unit tests for critical logic (parsers, date-range chunking, etc.).

How to add a new parser

1. Add a new module under `entsoe_api/parser/parser_extensions/` implementing `ParserInterface`.
2. Register the parser in `entsoe_api/parser/data_parser.py` by mapping the appropriate `DocumentType` to the parser class.
3. Add unit tests and usage examples demonstrating parser behavior.

Preparing a pull request

- Ensure all tests pass and code is linted.
- Update `CHANGELOG.md` with a summary of changes.
- Provide a clear description of the changes in the PR, including any new features, bug fixes, or breaking changes.
- Run the library locally and test the CLI with example commands to verify expected behavior.
- Run `pre-commit` hooks to ensure code quality and consistency.
- Run `pytest` from the project root to ensure all tests pass before submitting the PR.
- Update badges in the README if necessary (e.g., if you added new tests or changed coverage).

Updating badges

After running tests and generating coverage reports, you can update the badges in the README using the `genbadge` tool. For example:
```bash
genbadge coverage  -i .reports\coverage.xml -o docs/badges/coverage-badge.svg
genbadge tests -i .reports\junit.xml -o docs/badges/test-badge.svg
```

Development tips

- When modifying parsing logic, include small example XML samples and expected DataFrame assertions in tests.
- Keep CLI behavior backward compatible where possible. Document breaking changes in `CHANGELOG.md`.
- Run the library locally via `python -m entsoe_api.scripts.entsoe_fetcher` for manual smoke tests.

---

Navigation

- [Back to Index](index.md)
- [Structure](structure.md)
- [API reference](api.md)
