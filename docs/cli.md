# CLI — entsoe_fetcher

File: `entsoe_api/scripts/entsoe_fetcher.py`

Overview

The `entsoe_fetcher` script provides a simple command-line interface to fetch data from the ENTSO-E Transparency Platform and save it as CSV.

Available options

- `--start-date` / `-s` (required): start date in YYYY-MM-DD format
- `--end-date` / `-e` (required): end date in YYYY-MM-DD format
- `--document-type` / `-d` (required): document type (e.g. ACTUAL_GENERATION_PER_TYPE, PRICE_DOCUMENT)
- `--process-type` / `-p` (required): process type (e.g. A01, DAY_AHEAD, REALISED)
- `--in-domain` / `-i` (required): incoming domain code (from `DomainType`)
- `--out-domain` / `-o` (optional): outgoing domain code (from `DomainType`)
- `--psr-type` / `-r` (optional): PSR type (default: ALL)
- `--output` / `-f` (optional): output file path; if omitted the filename is auto-generated
- `--api-key` / `-k` (required): ENTSO-E API key
- `--chunk_size` / `-c` (optional): maximum period (days) for a single API request (default: 30)

Examples

- Fetch generation data for DE using default chunk size:

```bash
python -m entsoe_api.scripts.entsoe_fetcher \
  -s 2025-01-01 -e 2025-01-02 -d ACTUAL_GENERATION_PER_TYPE -p A01 -i DE -k $ENTSOE_KEY
```

- Fetch prices between two domains and save to a specific file:

```bash
python -m entsoe_api.scripts.entsoe_fetcher \
  -s 2025-01-01 -e 2025-01-10 -d PRICE_DOCUMENT -p A01 -i DE -o FR -r ALL -f prices-de-fr.csv -k $ENTSOE_KEY -c 7
```

Behavior and errors

- The script logs messages via `entsoe_api.utils.LOGGER`.
- API errors are caught and logged as `Error fetching data from ENTSO-E API`.

---

Navigation

- [Back to Index](index.md)
- [Usage (Quickstart)](usage.md)
- [API reference](api.md)

See [Usage](usage.md) for a quickstart and [API](api.md) for developer details.
