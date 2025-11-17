# For Developers

This section is for contributors who want to develop the project locally.

Quick environment setup

1. Create and activate a virtual environment (optional):

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the package in editable mode and other dependencies:

```bash
pip install -e .
```

Running tests and linters

- Tests: (if provided) run `pytest` from the project root.
- Linting: use `flake8`, `ruff` or your preferred linter according to project configuration.

Style and conventions

- Type hints: the project targets Python 3.10+ and uses type annotations (including new union syntax). Prefer typed interfaces and add type hints for public functions and classes.
- New features: add unit tests for critical logic (parsers, date-range chunking logic).

How to add a new parser

1. Add a new module under `entsoe_api/parser/parser_extensions/` implementing `ParserInterface`.
2. Register the parser in `entsoe_api/parser/data_parser.py` by mapping the appropriate `DocumentType` to the parser class.
3. Add unit tests and usage examples demonstrating parser behavior.

Preparing a release

- Update `CHANGELOG.md` and `pyproject.toml` with the new version number.
- Commit and tag the release, then push tags to the remote:

```bash
git add -A
git commit -m "Release vX.Y.Z"
git tag vX.Y.Z
git push --follow-tags
```

Development tips

- When modifying parsing logic, include small example XML samples and expected DataFrame assertions in tests.
- Keep CLI behavior backward compatible where possible. Document any breaking changes in `CHANGELOG.md`.
- Run the library locally via `python -m entsoe_api.scripts.entsoe_fetcher` for manual smoke tests.

---

Navigation

- [Back to Index](index.md)
- [Structure](structure.md)
- [API reference](api.md)
