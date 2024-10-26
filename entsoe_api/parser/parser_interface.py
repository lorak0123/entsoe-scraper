from abc import ABC, abstractmethod

import pandas as pd


class ParserInterface(ABC):
    @classmethod
    @abstractmethod
    def parse(cls, xml_data: bytes) -> pd.DataFrame:
        ...

    @staticmethod
    def _get_namespace(xml_data: bytes) -> dict:
        """
        Extracts the XML namespace from the data.

        Args:
            xml_data (bytes): The raw XML data.

        Returns:
            dict: Namespace for the XML parsing.
        """
        namespace = {'ns': xml_data.decode('utf-8').split('xmlns="')[1].split('"')[0]}
        return namespace

    @staticmethod
    def _get_resolution_interval(resolution: str) -> int:
        """
        Converts the resolution (e.g., 'PT60M', 'PT15M') to the corresponding number of minutes.

        Args:
            resolution (str): The time resolution in ISO 8601 duration format.

        Returns:
            int: The interval in minutes.
        """
        if resolution.startswith('PT'):
            if 'H' in resolution:
                return int(resolution.split('PT')[1].replace('H', '')) * 60  # Hours to minutes
            elif 'M' in resolution:
                return int(resolution.split('PT')[1].replace('M', ''))  # Minutes
        raise ValueError(f"Unsupported resolution format: {resolution}")
