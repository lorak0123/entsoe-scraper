import requests
import xml.etree.ElementTree as ET
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
    MAX_PERIOD_DAYS = 30
    REQUEST_DELAY = 0.5

    def __init__(self, api_key: str):
        """Initializes the EntsoeAPI with the given API key.

        Args:
            api_key (str): Your API key from the ENTSO-E Transparency Platform.
        """
        self.api_key = api_key
        self.data_parser = DataParser()

    def _get_data(
            self, start_date: datetime, end_date: datetime, document_type: DocumentType,
            process_type: ProcessType, domain: DomainType, psr_type: PsrType = 'ALL',
    ) -> bytes:
        """Fetches data from the ENTSO-E API.

        This method constructs the request to fetch energy production data between the specified start and end dates.

        Args:
            start_date (datetime): The start date and time of the data request.
            end_date (datetime): The end date and time of the data request.
            document_type (DocumentType): The type of document to request.
            process_type (ProcessType): The type of process to request.
            domain (DomainType): The domain code to specify the area.
            psr_type (PsrType, optional): The type of generation source. Defaults to 'ALL'.

        Returns:
            bytes: The raw XML data returned by the ENTSO-E API.

        Raises:
            EntsoeApiError: An error occurred while fetching the data.
        """
        params = {
            'documentType': document_type.value,
            'processType': process_type.value,
            'in_Domain': domain.value,
            'out_Domain': domain.value,
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
            process_type: ProcessType, domain: DomainType, psr_type: PsrType = 'ALL',
    ) -> pd.DataFrame:
        """Fetches data from the ENTSO-E API.

        This method constructs the request to fetch energy production data between the specified start and end dates.

        Args:
            start_date (datetime): The start date and time of the data request.
            end_date (datetime): The end date and time of the data request.
            document_type (DocumentType): The type of document to request.
            process_type (ProcessType): The type of process to request.
            domain (DomainType): The domain code to specify the area.
            psr_type (PsrType, optional): The type of generation source. Defaults to 'ALL'.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the production data.

        Raises:
            EntsoeApiError: An error occurred while fetching the data.
            CodeBindingError: An error occurred while parsing the XML data.
        """

        delta_days = (end_date - start_date).days

        if delta_days > self.MAX_PERIOD_DAYS:
            LOGGER.debug(f'Date range exceeds {self.MAX_PERIOD_DAYS} days. Splitting the request.')

            # Split the date range into chunks of at most MAX_PERIOD_DAYS days
            data_frames = []

            for i in range(0, delta_days, self.MAX_PERIOD_DAYS):
                chunk_start = start_date + timedelta(days=i)
                next_step = chunk_start + timedelta(
                    days=self.MAX_PERIOD_DAYS - 1
                    if document_type == DocumentType.PRICE_DOCUMENT
                    else self.MAX_PERIOD_DAYS
                )
                chunk_end = min(next_step, end_date)

                data_frames.append(
                    self.fetch_data(chunk_start, chunk_end, document_type, process_type, domain, psr_type))

            return pd.concat(data_frames)
        else:
            LOGGER.debug('Fetching data from ENTSO-E API...')
            xml_data = self._get_data(start_date, end_date, document_type, process_type, domain, psr_type)
            LOGGER.debug('Parsing data...')
            df = self.data_parser.parse_data(xml_data, document_type)
            return df
