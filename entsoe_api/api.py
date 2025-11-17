import requests
import pandas as pd
from datetime import datetime, timedelta

from entsoe_api.enums import ProcessType, PsrType, DocumentType, DomainType
from entsoe_api.exceptions import EntsoeApiError
from entsoe_api.parser.data_parser import DataParser
from entsoe_api.utils import LOGGER


class EntsoeAPI:
    """A class for interacting with the ENTSO-E API.

    This class allows you to fetch energy production data from the ENTSO-E Transparency Platform using the provided API key.

    Attributes:
        api_key (str): The API key for authentication.
    """

    BASE_URL = 'https://web-api.tp.entsoe.eu/api'
    REQUEST_DELAY = 0.5

    def __init__(self, api_key: str, max_period_days: int = 30):
        """Initializes the EntsoeAPI with the given API key.

        Args:
            api_key (str): Your API key from the ENTSO-E Transparency Platform.
        """
        self.api_key = api_key
        self.data_parser = DataParser()
        self.max_period_days = max_period_days

    def _get_data(
            self, start_date: datetime, end_date: datetime, document_type: DocumentType,
            process_type: ProcessType, in_domain: DomainType, out_domain: DomainType, psr_type: PsrType = 'ALL',
    ) -> bytes:
        """Fetches data from the ENTSO-E API.

        This method constructs the request to fetch energy production data between the specified start and end dates.

        Args:
            start_date (datetime): The start date and time of the data request.
            end_date (datetime): The end date and time of the data request.
            document_type (DocumentType): The type of document to request.
            process_type (ProcessType): The type of process to request.
            in_domain (DomainType): The domain code to specify the area.
            out_domain (DomainType): The domain code to specify the area.
            psr_type (PsrType, optional): The type of generation source. Defaults to 'ALL'.

        Returns:
            bytes: The raw XML data returned by the ENTSO-E API.

        Raises:
            EntsoeApiError: An error occurred while fetching the data.
        """
        params = {
            'documentType': document_type.value,
            'processType': process_type.value,
            'in_Domain': in_domain.value,
            'out_Domain': out_domain.value,
            'OutBiddingZone_Domain': in_domain.value,
            'periodStart': start_date.strftime('%Y%m%d%H00'),
            'periodEnd': end_date.strftime('%Y%m%d%H00'),
            'securityToken': self.api_key
        }

        if psr_type != 'ALL':
            params['psrType'] = psr_type.value

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code == 200:
            return response.content
        else:
            raise EntsoeApiError(f"API request failed with status code {response.status_code}: {response.text}")

    def fetch_data(
            self, start_date: datetime, end_date: datetime, document_type: DocumentType,
            process_type: ProcessType, in_domain: DomainType, out_domain: DomainType | None = None, psr_type: PsrType = 'ALL',
    ) -> pd.DataFrame:
        """Fetches data from the ENTSO-E API.

        This method constructs the request to fetch energy production data between the specified start and end dates.

       Args:
            start_date (datetime): The start date and time of the data request.
            end_date (datetime): The end date and time of the data request.
            document_type (DocumentType): The type of document to request.
            process_type (ProcessType): The type of process to request.
            in_domain (DomainType): The domain code to specify the area for incoming data.
            out_domain (DomainType, optional): The domain code to specify the area for outgoing data. Defaults to None.
            psr_type (PsrType, optional): The type of generation source. Defaults to 'ALL'.
        Returns:
            pd.DataFrame: A pandas DataFrame containing the production data.

        Raises:
            EntsoeApiError: An error occurred while fetching the data.
            CodeBindingError: An error occurred while parsing the XML data.
        """

        delta_days = (end_date - start_date).days

        if delta_days > self.max_period_days:
            LOGGER.debug(f'Date range exceeds {self.max_period_days} days. Splitting the request.')

            # Split the date range into chunks of at most MAX_PERIOD_DAYS days
            data_frames = []

            for i in range(0, delta_days, self.max_period_days):
                chunk_start = start_date + timedelta(days=i)
                next_step = chunk_start + timedelta(
                    days=self.max_period_days - 1
                    if document_type == DocumentType.PRICE_DOCUMENT
                    else self.max_period_days
                )
                chunk_end = min(next_step, end_date - timedelta(days=1) if document_type == DocumentType.PRICE_DOCUMENT else end_date)

                data_frames.append(
                    self.fetch_data(chunk_start, chunk_end, document_type, process_type, in_domain, out_domain, psr_type)
                )

            return pd.concat(data_frames)
        else:
            LOGGER.debug(f'Fetching data from ENTSO-E API for {start_date} to {end_date}...')
            xml_data = self._get_data(
                start_date=start_date,
                end_date=end_date,
                document_type=document_type,
                process_type=process_type,
                in_domain=in_domain,
                out_domain=out_domain if out_domain is not None else in_domain,
                psr_type=psr_type
            )
            df = self.data_parser.parse_data(xml_data, document_type)
            return df
