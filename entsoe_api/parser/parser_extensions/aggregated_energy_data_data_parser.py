from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import pandas as pd

from entsoe_api.enums import PsrType
from entsoe_api.parser.parser_interface import ParserInterface


class AggregatedEnergyDataDataParser(ParserInterface):
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

        res_data = pd.DataFrame()

        time_series_elements = root.findall('.//ns:TimeSeries', namespace)

        unit = time_series_elements[0].find('.//ns:quantity_Measure_Unit.name', namespace).text

        for period in time_series_elements:
            start_date = datetime.strptime(period.find('.//ns:Period/ns:timeInterval/ns:start', namespace).text,
                                           '%Y-%m-%dT%H:%MZ')
            end_date = datetime.strptime(period.find('.//ns:Period/ns:timeInterval/ns:end', namespace).text,
                                            '%Y-%m-%dT%H:%MZ')

            resolution = period.find('.//ns:Period/ns:resolution', namespace).text
            interval_minutes = cls._get_resolution_interval(resolution)

            data_rows = []

            for point in period.findall('.//ns:Period/ns:Point', namespace):
                position = int(point.find('ns:position', namespace).text)
                quantity = float(point.find('ns:quantity', namespace).text)

                data_rows.append({
                    'timestamp': start_date + timedelta(minutes=interval_minutes * (position - 1)),
                    'unit': unit,
                    'resolution': resolution,
                    'Quantity': quantity
                })

            df = pd.DataFrame(data_rows)
            df.set_index('timestamp', inplace=True)
            idx = pd.date_range(start=start_date, end=end_date - timedelta(minutes=interval_minutes), freq=f'{interval_minutes}min')
            df = df.reindex(idx).fillna(0).rename_axis(index='timestamp')

            res_data = pd.concat([res_data, df])

        return res_data
