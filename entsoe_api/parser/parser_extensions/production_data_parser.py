"""Production data parser for XML returned by the ENTSO-E API."""

from datetime import datetime, timedelta

import pandas as pd
from defusedxml import ElementTree

from build.lib.entsoe_api.utils import LOGGER
from entsoe_api.enums import PsrType
from entsoe_api.parser.parser_interface import ParserInterface


class ProductionDataParser(ParserInterface):
    """A parser for production data XML returned by the ENTSO-E API."""

    @classmethod
    def parse(cls, xml_data: bytes) -> pd.DataFrame:
        """Parse production data XML from ENTSO-E API into a pandas DataFrame.

        Args:
            xml_data (bytes): The XML data returned by the ENTSO-E API.

        Returns:
            pd.DataFrame: Production data in a DataFrame format.

        """
        namespace = cls._get_namespace(xml_data)
        root = ElementTree.fromstring(xml_data)

        data_rows = []

        time_series_elements = root.findall(".//ns:TimeSeries", namespace)

        for time_series in time_series_elements:
            for period in time_series.findall(".//ns:Period", namespace):
                psr_type = time_series.find(".//ns:psrType", namespace).text
                start_date = datetime.strptime(
                    period.find("ns:timeInterval/ns:start", namespace).text, "%Y-%m-%dT%H:%MZ"
                )
                end_date = datetime.strptime(period.find("ns:timeInterval/ns:end", namespace).text, "%Y-%m-%dT%H:%MZ")

                resolution = period.find("ns:resolution", namespace).text
                interval_minutes = cls._get_resolution_interval(resolution)

                for point in period.findall("ns:Point", namespace):
                    position = int(point.find("ns:position", namespace).text)
                    quantity = float(point.find("ns:quantity", namespace).text)

                    data_rows.append(
                        {
                            "timestamp": start_date + timedelta(minutes=interval_minutes * position),
                            "PsrType": PsrType(psr_type).name,
                            "Quantity": quantity,
                        }
                    )

                if data_rows[-1]["timestamp"] >= end_date:
                    LOGGER.warning(
                        f"Data point timestamp {data_rows[-1]['timestamp']} exceeds "
                        f"the end date {end_date} for psrType {psr_type}."
                        "\nThis may indicate an issue with the data or the resolution interval."
                    )

        df = pd.DataFrame(data_rows)
        df = (
            df.groupby(["timestamp", "PsrType"], as_index=False)
            .sum()
            .pivot(index="timestamp", columns="PsrType", values="Quantity")
            .fillna(0)
        )

        return df.sort_index()
