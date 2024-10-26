from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import pandas as pd

from entsoe_api.enums import PsrType
from entsoe_api.parser.parser_interface import ParserInterface


class ProductionDataParser(ParserInterface):
    @classmethod
    def parse(cls, xml_data: bytes) -> pd.DataFrame:
        """
        Parses production data XML from ENTSO-E API into a pandas DataFrame.

        Args:
            xml_data (bytes): The XML data returned by the ENTSO-E API.

        Returns:
            pd.DataFrame: Production data in a DataFrame format.
        """
        namespace = cls._get_namespace(xml_data)
        root = ET.fromstring(xml_data)

        data_rows = []

        time_series_elements = root.findall('.//ns:TimeSeries', namespace)

        for period in time_series_elements:
            psr_type = period.find('.//ns:psrType', namespace).text
            start_date = datetime.strptime(period.find('.//ns:timeInterval/ns:start', namespace).text,
                                           '%Y-%m-%dT%H:%MZ')
            resolution = period.find('.//ns:resolution', namespace).text
            interval_minutes = cls._get_resolution_interval(resolution)

            for point in period.findall('.//ns:Point', namespace):
                position = int(point.find('ns:position', namespace).text)
                quantity = float(point.find('ns:quantity', namespace).text)

                data_rows.append({
                    'timestamp': start_date + timedelta(minutes=interval_minutes * (position - 1)),
                    'PsrType': PsrType(psr_type).name,
                    'Quantity': quantity
                })

        df = pd.DataFrame(data_rows)
        df = df.groupby(
            ['timestamp', 'PsrType'], as_index=False
        ).sum().pivot(index='timestamp', columns='PsrType', values='Quantity').fillna(0)

        return df.sort_index()
