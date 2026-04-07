"""Module for parsing the data returned by the ENTSO-E API.

The DataParser class maintains a mapping of document types to their respective parsers,
allowing it to handle different types of data returned by the ENTSO-E API. The parse_data method takes XML data
and a document type as input and returns the parsed data in a DataFrame format.
If a parser for the specified document type is not defined, it raises a ParserError.
"""

import pandas as pd

from entsoe_api.enums import DocumentType
from entsoe_api.parser.exceptions import ParserError
from entsoe_api.parser.parser_extensions.aggregated_energy_data_data_parser import AggregatedEnergyDataDataParser
from entsoe_api.parser.parser_extensions.price_data_parser import PriceDataParser
from entsoe_api.parser.parser_extensions.production_data_parser import ProductionDataParser
from entsoe_api.parser.parser_extensions.total_load_data_parser import TotalLoad
from entsoe_api.parser.parser_interface import ParserInterface, TimeSeriesData


class DataParser:
    """A class for parsing various types of XML data into pandas DataFrame."""

    PARSERS: dict[DocumentType, type[ParserInterface]] = {
        DocumentType.ACTUAL_GENERATION_PER_TYPE: ProductionDataParser,
        DocumentType.PRICE_DOCUMENT: PriceDataParser,
        DocumentType.AGGREGATED_ENERGY_DATA_REPORT: AggregatedEnergyDataDataParser,
        DocumentType.WIND_AND_SOLAR_FORECAST: ProductionDataParser,
        DocumentType.SYSTEM_TOTAL_LOAD: TotalLoad,
    }

    @classmethod
    def parse_to_raw_data(cls, xml_data: bytes, document_type: DocumentType) -> list[TimeSeriesData]:
        """Parse the XML data based on document type and returns a pandas DataFrame.

        Args:
            xml_data (bytes): The XML data to parse.
            document_type (DocumentType): The type of document to parse.

        Returns:
            pd.DataFrame: Parsed data in DataFrame format.

        """
        if document_type not in cls.PARSERS:
            raise ParserError(f"Parser for document type '{document_type}' is not defined.")

        # Get the specific parser for the document type
        return cls.PARSERS[document_type].parse(xml_data)

    @classmethod
    def parse_to_dataframe(
        cls, xml_data: bytes, document_type: DocumentType, include_metadata: bool = False
    ) -> pd.DataFrame:
        """Parse the XML data based on document type and returns a pandas DataFrame.

        It is important that to convert data to a DataFrame, the data needs to have same timestamps for all time series.
            In case of missing timestamps or datasets with different resolution,
            the missing timestamps will be filled with NaN values.

        Args:
            xml_data (bytes): The XML data to parse.
            document_type (DocumentType): The type of document to parse.
            include_metadata (bool, optional): Whether to include metadata in the DataFrame. Defaults to False.

        Returns:
            pd.DataFrame: Parsed data in DataFrame format.

        """
        raw_data = cls.parse_to_raw_data(xml_data, document_type)

        # Create a DataFrame from the raw data
        df = pd.DataFrame(
            {
                "timestamp": [timestamp for time_series in raw_data for timestamp, _ in time_series.data],
                "value": [value for time_series in raw_data for _, value in time_series.data],
                "series_name": [time_series.name for time_series in raw_data for _ in time_series.data],
            }
        )

        # Pivot the DataFrame to have series names as columns and timestamps as index
        df_pivot = df.pivot(index="timestamp", columns="series_name", values="value")

        if include_metadata:
            # Add metadata columns to the DataFrame
            for time_series in raw_data:
                df_pivot[f"{time_series.name}-data_end"] = None
                df_pivot.at[min(timestamp for timestamp, _ in time_series.data), f"{time_series.name}-data_end"] = max(
                    timestamp for timestamp, _ in time_series.data
                )
                for key, value in time_series.metadata.items():
                    if f"{time_series.name}-{key}" not in df_pivot.columns:
                        df_pivot[f"{time_series.name}-{key}"] = None
                    df_pivot.at[min(timestamp for timestamp, _ in time_series.data), f"{time_series.name}-{key}"] = (
                        value
                    )

        return df_pivot

    @classmethod
    def parse_data_to_dataframe_set(
        cls, xml_data: bytes, document_type: DocumentType, include_metadata: bool = True
    ) -> list[pd.DataFrame]:
        """Parse the XML data based on document type and returns a set of pandas DataFrames.

        Args:
            xml_data (bytes): The XML data to parse.
            document_type (DocumentType): The type of document to parse.
            include_metadata (bool, optional): Whether to include metadata in the DataFrame. Defaults to False.

        Returns:
            set[pd.DataFrame]: A set of parsed data in DataFrame format.

        """
        raw_data = cls.parse_to_raw_data(xml_data, document_type)
        dataframes = {}

        for time_series in raw_data:
            df = pd.DataFrame(
                {
                    "timestamp": [timestamp for timestamp, _ in time_series.data],
                    time_series.name: [value for _, value in time_series.data],
                }
            ).set_index("timestamp")

            if time_series.name in dataframes:
                dataframes[time_series.name] = pd.concat([dataframes[time_series.name], df])
            else:
                dataframes[time_series.name] = df

            if include_metadata:
                df = pd.DataFrame(
                    {
                        "timestamp": [min(timestamp for timestamp, _ in time_series.data)],
                        f"{time_series.name}-data_end": [max(timestamp for timestamp, _ in time_series.data)],
                    }
                ).set_index("timestamp")

                if f"{time_series.name}-data_end" in dataframes:
                    dataframes[f"{time_series.name}-data_end"] = pd.concat(
                        [dataframes[f"{time_series.name}-data_end"], df]
                    )
                else:
                    dataframes[f"{time_series.name}-data_end"] = df

                for key, value in time_series.metadata.items():
                    df = pd.DataFrame(
                        {
                            "timestamp": [min(timestamp for timestamp, _ in time_series.data)],
                            f"{time_series.name}-{key}": [value],
                        }
                    ).set_index("timestamp")

                    if f"{time_series.name}-{key}" in dataframes:
                        dataframes[f"{time_series.name}-{key}"] = pd.concat(
                            [dataframes[f"{time_series.name}-{key}"], df]
                        )
                    else:
                        dataframes[f"{time_series.name}-{key}"] = df

        return dataframes
