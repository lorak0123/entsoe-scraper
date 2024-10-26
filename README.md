# ENTSO-E API Data Fetcher

A Python package for fetching and parsing energy production data from the ENTSO-E Transparency Platform API. This tool
provides an easy-to-use interface to retrieve data and output it in a structured format using `pandas`.

---

## Key Features

- **Flexible Data Retrieval:** Supports fetching and parsing various document types, including generation, production
  per type, and pricing data.
- **Automatic Date Chunking:** Handles large date ranges by splitting requests into manageable chunks.
- **Interval Detection:** Automatically parses and applies the data interval from XML responses.
- **Convenient CLI Tool:** Includes a command-line interface (CLI) for quick data fetching and saving.

---

## Installation

To install the package, clone this repository and install it using `pip`:

```bash
git clone https://github.com/your-username/entsoe-api.git
cd entsoe-api
pip install .
```

## Usage

### Command Line Interface (CLI)

The `entsoe-fetcher` command-line tool allows you to fetch data and save it to a file.

#### Example Command

```bash
entsoe-fetcher -s 2022-01-01 -e 2024-10-01 -d ACTUAL_GENERATION_PER_TYPE -p REALISED -m DE -o actual_gen_per_type_realised.csv -k YOUR_API_KEY
```

#### CLI Options

| Flag | Description                                        |
|------|----------------------------------------------------|
| `-s` | Start date (e.g., `2022-01-01`)                    |
| `-e` | End date (e.g., `2024-10-01`)                      |
| `-d` | Document type (e.g., `ACTUAL_GENERATION_PER_TYPE`) |
| `-p` | Process type (e.g., `REALISED`)                    |
| `-m` | Market domain (e.g., `DE`)                         |
| `-o` | Output CSV filename                                |
| `-k` | Your ENTSO-E API key                               |

---

## Code Example

To use the `EntsoeAPI` class programmatically, create an instance and call `fetch_data` with the required parameters:

```python
from entsoe_api.api import EntsoeAPI
from entsoe_api.enums import DocumentType, ProcessType, DomainType, PsrType
from datetime import datetime

api = EntsoeAPI(api_key="YOUR_API_KEY")

start_date = datetime(2022, 1, 1)
end_date = datetime(2022, 1, 31)
document_type = DocumentType.ACTUAL_GENERATION_PER_TYPE
process_type = ProcessType.REALISED
domain = DomainType.DE

data = api.fetch_data(start_date, end_date, document_type, process_type, domain)
data.to_csv("output.csv", index=False)
```

---

## Project Structure

- **entsoe_api/api.py**: Core API interaction logic
- **entsoe_api/parser**: XML parsers for various document types
- **scripts/entsoe_fetcher.py**: CLI entry point
- **entsoe_api/enums**: Enums defining document, process, and domain types
- **entsoe_api/exceptions.py**: Custom exceptions

---

## Documentation

For complete documentation, see the `docs/` directory.

---

## License

This project is licensed under the MIT License.
