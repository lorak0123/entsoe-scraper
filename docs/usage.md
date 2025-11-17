# Usage (Quickstart)

A short guide on fetching data from ENTSO-E using this project.

Requirements

- Python 3.10+ (the project uses union types and modern type annotations)
- Project dependencies installed (see `pyproject.toml`)
- ENTSO-E API key

Quickstart

1. Install dependencies: `pip install -e .` or `pip install -r requirements.txt` (if you have a requirements file).
2. Run the CLI to fetch data:

```bash
python -m entsoe_api.scripts.entsoe_fetcher \
  --start-date 2025-01-01 \
  --end-date 2025-01-02 \
  --document-type ACTUAL_GENERATION_PER_TYPE \
  --process-type A01 \
  --in-domain DE \
  --psr-type ALL \
  --api-key <YOUR_API_KEY>
```

3. The CSV file will be saved in the current directory (unless you pass `--output/-f`).

Tips

- Use `--chunk_size` to adjust the maximum period (in days) for a single API request.
- If you want to fetch data between two different bidding zones, pass both `--in-domain` and `--out-domain`.

See [CLI](cli.md) for the full list of options and [API](api.md) for programmatic usage.

---

Navigation

- [Back to Index](index.md)
- [CLI reference](cli.md)
- [API reference](api.md)
