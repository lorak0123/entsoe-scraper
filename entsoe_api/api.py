"""EntsoeAPI - A Python client for the ENTSO-E API.

Module that provides the `EntsoeAPI` class for interacting with the ENTSO-E API.
The `EntsoeAPI` class allows users to fetch energy production data from the ENTSO-E Transparency Platform
using a provided API key. It handles the construction of API requests, manages date range splitting for
large requests, and parses the XML responses into pandas DataFrames for easy analysis.
"""

from datetime import datetime, timedelta
from typing import Literal

import pandas as pd
import requests

from entsoe_api.enums import DocumentType, DomainType, ProcessType, PsrType
from entsoe_api.exceptions import EntsoeApiError
from entsoe_api.parser.data_parser import DataParser
from entsoe_api.parser.parser_interface import TimeSeriesData
from entsoe_api.utils import LOGGER


class EntsoeAPI:
    """A class for interacting with the ENTSO-E API.

    This class allows you to fetch energy production data from the
        ENTSO-E Transparency Platform using the provided API key.

    Attributes:
        api_key (str): The API key for authentication.

    """

    BASE_URL = "https://web-api.tp.entsoe.eu/api"
    REQUEST_DELAY = 0.5

    def __init__(
        self,
        api_key: str,
        max_period_days: int = 30,
        return_format: Literal["raw", "dataframe", "dataframe_set"] = "raw",
    ):
        """Initialize the EntsoeAPI with the given API key.

        Args:
            api_key (str): Your API key from the ENTSO-E Transparency Platform.
            max_period_days (int, optional): The maximum number of days to request in a single API call. Defaults to 30.
            return_format (Literal["raw", "dataframe", "dataframe_set"], optional): The format in which to return the
                data.
                - "raw": Return the raw parsed data as a list of TimeSeriesData objects.
                - "dataframe": Return the data as a single pandas DataFrame.
                - "dataframe_set": Return the data as a dictionary of pandas DataFrames, where each key corresponds
                    to a different time series. Defaults to "raw".


        """
        self.api_key = api_key
        self.max_period_days = max_period_days
        self.return_format = return_format

    def _get_data(
        self,
        start_date: datetime,
        end_date: datetime,
        document_type: DocumentType,
        process_type: ProcessType,
        in_domain: DomainType,
        out_domain: DomainType,
        psr_type: PsrType = "ALL",
    ) -> bytes:
        """Fetch data from the ENTSO-E API.

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
            "documentType": document_type.value,
            "processType": process_type.value,
            "in_Domain": in_domain.value,
            "out_Domain": out_domain.value,
            "OutBiddingZone_Domain": in_domain.value,
            "periodStart": start_date.strftime("%Y%m%d%H00"),
            "periodEnd": end_date.strftime("%Y%m%d%H00"),
            "securityToken": self.api_key,
        }

        if psr_type != "ALL":
            params["psrType"] = psr_type.value

        response = requests.get(self.BASE_URL, params=params, timeout=60)

        if response.status_code == 200:
            return response.content
        else:
            raise EntsoeApiError(f"API request failed with status code {response.status_code}: {response.text}")

    def fetch_data(
        self,
        start_date: datetime,
        end_date: datetime,
        document_type: DocumentType,
        process_type: ProcessType,
        in_domain: DomainType,
        out_domain: DomainType | None = None,
        psr_type: PsrType = "ALL",
        include_metadata: bool = False,
    ) -> pd.DataFrame:
        """Fetch data from the ENTSO-E API.

         This method constructs the request to fetch energy production data between the specified start and end dates.

        Args:
            start_date (datetime): The start date and time of the data request.
            end_date (datetime): The end date and time of the data request.
            document_type (DocumentType): The type of document to request.
            process_type (ProcessType): The type of process to request.
            in_domain (DomainType): The domain code to specify the area for incoming data.
            out_domain (DomainType, optional): The domain code to specify the area for outgoing data. Defaults to None.
            psr_type (PsrType, optional): The type of generation source. Defaults to 'ALL'.
            include_metadata (bool, optional): Whether to include metadata in the returned DataFrame. Defaults to False.

        Returns:
            pd.DataFrame: A pandas DataFrame containing the production data.

        Raises:
            EntsoeApiError: An error occurred while fetching the data.
            CodeBindingError: An error occurred while parsing the XML data.

        """
        delta_days = (end_date - start_date).days

        if delta_days > self.max_period_days:
            LOGGER.debug(f"Date range exceeds {self.max_period_days} days. Splitting the request.")

            # Split the date range into chunks of at most MAX_PERIOD_DAYS days
            data_frames = []

            for i in range(0, delta_days, self.max_period_days):
                chunk_start = start_date + timedelta(days=i)
                next_step = chunk_start + timedelta(
                    days=self.max_period_days - 1
                    if document_type == DocumentType.PRICE_DOCUMENT
                    else self.max_period_days
                )
                chunk_end = min(
                    next_step,
                    end_date - timedelta(days=1) if document_type == DocumentType.PRICE_DOCUMENT else end_date,
                )

                data_frames.append(
                    self.fetch_data(
                        chunk_start,
                        chunk_end,
                        document_type,
                        process_type,
                        in_domain,
                        out_domain,
                        psr_type,
                        include_metadata,
                    )
                )

            res = self._merge_results(data_frames)
        else:
            LOGGER.debug(f"Fetching data from ENTSO-E API for {start_date} to {end_date}...")
            xml_data = self._get_data(
                start_date=start_date,
                end_date=end_date,
                document_type=document_type,
                process_type=process_type,
                in_domain=in_domain,
                out_domain=out_domain if out_domain is not None else in_domain,
                psr_type=psr_type,
            )
            if self.return_format == "raw":
                res = DataParser.parse_to_raw_data(xml_data, document_type)
            elif self.return_format == "dataframe":
                res = DataParser.parse_to_dataframe(xml_data, document_type, include_metadata=include_metadata)
            elif self.return_format == "dataframe_set":
                res = DataParser.parse_data_to_dataframe_set(xml_data, document_type, include_metadata=include_metadata)
            else:
                raise ValueError(f"Invalid return format: {self.return_format}")

        return self._process_result(res)

    def _process_result(
        self, res: pd.DataFrame | dict[str, pd.DataFrame] | list[TimeSeriesData]
    ) -> pd.DataFrame | dict[str, pd.DataFrame] | list[TimeSeriesData]:
        if self.return_format == "dataframe":
            smallest_resolution = res.index.diff().min()
            if smallest_resolution == timedelta(0):
                LOGGER.warning(
                    "The smallest resolution of the time series data is 0, which may indicate duplicate timestamps."
                    "\nConsider checking the data for duplicates or missing timestamps."
                )
                res = res.groupby(res.index).first()  # Keep the first occurrence of duplicate timestamps

                smallest_resolution = res.index.diff().min()

            idx = pd.date_range(start=res.index.min(), end=res.index.max(), freq=smallest_resolution)
            res = res.reindex(idx, method="ffill").rename_axis(index="timestamp")

        return res

    def _merge_results(
        self, data_frames: list[pd.DataFrame] | list[dict[str, pd.DataFrame]] | list[list[TimeSeriesData]]
    ) -> pd.DataFrame | dict[str, pd.DataFrame] | list[TimeSeriesData]:

        if self.return_format == "dataframe":
            return pd.concat(data_frames)
        elif self.return_format == "dataframe_set":
            merged_dataframes = {}
            for df_set in data_frames:
                for key, df in df_set.items():
                    if key not in merged_dataframes:
                        merged_dataframes[key] = df
                    else:
                        merged_dataframes[key] = pd.concat([merged_dataframes[key], df])
            return merged_dataframes
        elif self.return_format == "raw":
            merged_raw_data = []
            for raw_data in data_frames:
                merged_raw_data.extend(raw_data)
            return merged_raw_data
