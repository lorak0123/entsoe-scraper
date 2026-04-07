"""Main script for fetching data from the ENTSO-E Transparency API and saving it to a CSV file."""

from datetime import datetime

import click
import pandas as pd

from entsoe_api.api import EntsoeAPI
from entsoe_api.enums import DocumentType, DomainType, ProcessType, PsrType
from entsoe_api.exceptions import EntsoeApiError
from entsoe_api.utils import LOGGER


@click.command()
@click.option("--start-date", "-s", required=True, help="Start date in format YYYY-MM-DD", type=str)
@click.option("--end-date", "-e", required=True, help="End date in format YYYY-MM-DD", type=str)
@click.option(
    "--document-type",
    "-dt",
    required=True,
    type=click.Choice([e.name for e in DocumentType]),
    help="DocumentType for the request.",
)
@click.option(
    "--process-type",
    "-pt",
    required=True,
    type=click.Choice([e.name for e in ProcessType]),
    help="ProcessType for the request.",
)
@click.option(
    "--in-domain",
    "-id",
    required=True,
    type=click.Choice([e.name for e in DomainType]),
    help="InDomainType for the request.",
)
@click.option(
    "--out-domain",
    "-od",
    default=None,
    type=click.Choice([e.name for e in DomainType]),
    help="OutDomainType for the request.",
)
@click.option(
    "--psr-type",
    "-rt",
    default="ALL",
    type=click.Choice([e.name for e in PsrType]),
    help="PsrType for the request. Defaults to ALL.",
)
@click.option("--output", "-o", help="Output file path for the CSV file.", type=str)
@click.option("--api-key", "-k", required=True, help="Your ENTSO-E API key.")
@click.option("--chunk_size", "-cs", default=30, help="Chunk size for fetching data.", type=int)
@click.option(
    "--format",
    "-f",
    default="csv",
    help="Output format (csv or xlsx). Defaults to csv.",
    type=click.Choice(["csv", "xlsx"]),
)
@click.option("--add_meta", "-m", is_flag=True, help="Whether to include metadata in the output file.")
def fetch_entsoe_data(
    start_date: str,
    end_date: str,
    document_type: str,
    process_type: str,
    in_domain: str,
    out_domain: str,
    psr_type: str,
    output: str,
    api_key: str,
    chunk_size: int,
    format: str,
    add_meta: bool,
):
    """Fetch data from the ENTSO-E Transparency API and save it to a CSV file."""
    try:
        # Convert input string dates to datetime objects
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")

        # Initialize the API client
        entsoe_api = EntsoeAPI(
            api_key,
            max_period_days=chunk_size,
            return_format="dataframe" if format == "csv" else "dataframe_set",
        )

        LOGGER.info(f"Fetching data from {start_date} to {end_date}...")

        # Fetch data from the API
        df = entsoe_api.fetch_data(
            start_date=start_date_dt,
            end_date=end_date_dt,
            document_type=DocumentType[document_type],
            process_type=ProcessType[process_type],
            in_domain=DomainType[in_domain],
            out_domain=DomainType[out_domain] if out_domain else None,
            psr_type=PsrType[psr_type] if psr_type != "ALL" else PsrType.ALL,
            include_metadata=add_meta,
        )

        if not output:
            output = f"{document_type}-{process_type}-{in_domain}-{out_domain}-{psr_type}-{start_date}-{end_date}"

        LOGGER.info(f"Saving data to {output}...")

        if format == "xlsx":
            with pd.ExcelWriter(f"{output}.xlsx") as writer:
                for name, df in df.items():
                    df.to_excel(writer, sheet_name=name)
        else:
            df.to_csv(f"{output}.csv", index=True)

        LOGGER.info(f"Data successfully saved to {output}")

    except EntsoeApiError as e:
        LOGGER.error(f"Error fetching data from ENTSO-E API: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error: {e}")
