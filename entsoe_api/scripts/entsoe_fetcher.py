import click
from datetime import datetime

from entsoe_api.api import EntsoeAPI
from entsoe_api.enums import DocumentType, ProcessType, PsrType, DomainType
from entsoe_api.exceptions import EntsoeApiError
from entsoe_api.utils import LOGGER


@click.command()
@click.option('--start-date', '-s', required=True, help="Start date in format YYYY-MM-DD", type=str)
@click.option('--end-date', '-e', required=True, help="End date in format YYYY-MM-DD", type=str)
@click.option('--document-type', '-d', required=True, type=click.Choice([e.name for e in DocumentType]),
              help="DocumentType for the request.")
@click.option('--process-type', '-p', required=True, type=click.Choice([e.name for e in ProcessType]),
              help="ProcessType for the request.")
@click.option('--domain', '-m', required=True, type=click.Choice([e.name for e in DomainType]),
              help="DomainType for the request.")
@click.option('--psr-type', '-r', default='ALL', type=click.Choice([e.name for e in PsrType]),
              help="PsrType for the request. Defaults to ALL.")
@click.option('--output', '-o', required=True, help="Output CSV file path.")
@click.option('--api-key', '-k', required=True, help="Your ENTSO-E API key.")
def fetch_entsoe_data(
        start_date: str,
        end_date: str,
        document_type: str,
        process_type: str,
        domain: str,
        psr_type: str,
        output: str,
        api_key: str,
):
    """
    Fetch data from the ENTSO-E Transparency API and save it to a CSV file.
    """
    try:
        # Convert input string dates to datetime objects
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')

        # Initialize the API client
        entsoe_api = EntsoeAPI(api_key)

        LOGGER.info(f"Fetching data from {start_date} to {end_date}...")

        # Fetch data from the API
        df = entsoe_api.fetch_data(
            start_date=start_date_dt,
            end_date=end_date_dt,
            document_type=DocumentType[document_type],
            process_type=ProcessType[process_type],
            domain=DomainType[domain],
            psr_type=PsrType[psr_type] if psr_type != 'ALL' else 'ALL'
        )

        LOGGER.info(f"Saving data to {output}...")

        # Save the DataFrame to CSV
        df.to_csv(output, index=True)

        LOGGER.info(f"Data successfully saved to {output}")

    except EntsoeApiError as e:
        LOGGER.error(f"Error fetching data from ENTSO-E API: {e}")
    except Exception as e:
        LOGGER.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    fetch_entsoe_data()
