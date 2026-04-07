"""Module defining the ParserInterface for parsing XML data into pandas DataFrames."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime, timedelta

from defusedxml import ElementTree

from entsoe_api.utils import LOGGER


@dataclass
class TimeSeriesData:
    """Data class to hold information about a time series."""

    name: str
    metadata: dict
    data: list[tuple[datetime, float]]


class ParserInterface(ABC):
    """Abstract base class for parsers that convert XML data into pandas DataFrames."""

    POINT_VALUE_TAG = "quantity"

    @classmethod
    @abstractmethod
    def _get_time_series_name(cls, time_series_element, namespace) -> str:
        """Extract the name of the time series from the XML element."""
        ...

    @classmethod
    @abstractmethod
    def _parse_metadata(cls, time_series_element, namespace) -> dict:
        """Extract metadata from the time series XML element."""
        ...

    @classmethod
    def _get_namespace(cls, xml_data: bytes) -> dict:
        """Extract the XML namespace from the data.

        Args:
            xml_data (bytes): The raw XML data.

        Returns:
            dict: Namespace for the XML parsing.

        """
        namespace = {"ns": xml_data.decode("utf-8").split('xmlns="')[1].split('"')[0]}
        return namespace

    @classmethod
    def _get_resolution_interval(cls, period_element, namespace) -> timedelta:
        """Convert the resolution (e.g., 'PT60M', 'PT15M') to the corresponding number of minutes.

        Args:
            period_element: The XML element containing the resolution information.
            namespace: The XML namespace for parsing.

        Returns:
            timedelta: The resolution interval as a timedelta object.

        """
        resolution = period_element.find("ns:resolution", namespace).text

        if resolution.startswith("PT"):
            if "H" in resolution:
                return timedelta(hours=int(resolution.split("PT")[1].replace("H", "")))
            elif "M" in resolution:
                return timedelta(minutes=int(resolution.split("PT")[1].replace("M", "")))
        elif resolution.startswith("P"):
            if "D" in resolution:
                return timedelta(days=int(resolution.split("P")[1].replace("D", "")))
            elif "W" in resolution:
                return timedelta(weeks=int(resolution.split("P")[1].replace("W", "")))
            elif "Y" in resolution:
                return timedelta(days=365 * int(resolution.split("P")[1].replace("Y", "")))

        raise ValueError(f"Unsupported resolution format: {resolution}")

    @classmethod
    def parse(cls, xml_data: bytes) -> list[TimeSeriesData]:
        """Parse the XML data and extract time series information.

        Args:
            xml_data: The raw XML data to be parsed.

        Returns: A list of TimeSeriesData objects containing the name, metadata,
            and data points for each time series found in the XML.

        """
        result = []

        namespace = cls._get_namespace(xml_data)
        root = ElementTree.fromstring(xml_data)

        time_series_elements = root.findall(".//ns:TimeSeries", namespace)

        for time_series in time_series_elements:
            tmp = TimeSeriesData(
                name=cls._get_time_series_name(time_series, namespace),
                metadata=cls._parse_metadata(time_series, namespace),
                data=[],
            )
            for period in time_series.findall(".//ns:Period", namespace):
                tmp.data.extend(cls._parse_single_period(period, namespace))

            result.append(tmp)

        return result

    @classmethod
    def _parse_single_period(cls, period_element, namespace) -> list:
        """Parse a single Period element and return a list of data rows."""
        data_rows = []

        start_date = datetime.strptime(
            period_element.find("ns:timeInterval/ns:start", namespace).text, "%Y-%m-%dT%H:%MZ"
        )
        end_date = datetime.strptime(period_element.find("ns:timeInterval/ns:end", namespace).text, "%Y-%m-%dT%H:%MZ")

        resolution = cls._get_resolution_interval(period_element, namespace)

        for point in period_element.findall("ns:Point", namespace):
            position = int(point.find("ns:position", namespace).text)
            quantity = float(point.find(f"ns:{cls.POINT_VALUE_TAG}", namespace).text)

            data_rows.append(
                (
                    start_date + resolution * (position - 1),
                    quantity,
                )
            )

        if data_rows[-1][0] >= end_date:
            LOGGER.warning(
                f"Data point timestamp {data_rows[-1][0]} exceeds the end date {end_date}."
                "\nThis may indicate an issue with the data or the resolution interval."
            )

        return data_rows
