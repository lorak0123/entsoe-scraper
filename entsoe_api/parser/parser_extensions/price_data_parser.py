from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
import pandas as pd

from entsoe_api.parser.parser_interface import ParserInterface


class PriceDataParser(ParserInterface):
    @classmethod
    def _fill_gaps(cls, df: pd.DataFrame, interval: int, time_start: datetime, time_end: datetime) -> pd.DataFrame:
        """
        Fills the gaps in the DataFrame by resampling the data to a 15-minute interval.

        Args:
            df (pd.DataFrame): The DataFrame to fill the gaps in.
            interval (int): The interval in minutes.
            time_start (datetime): The start date and time of the data.
            time_end (datetime): The end date and time of the data.

        Returns:
            pd.DataFrame: The DataFrame with gaps filled.
        """
        idx = pd.date_range(start=time_start, end=time_end - timedelta(minutes=interval), freq=f'{interval}min')
        return df.reindex(idx, method='ffill').rename_axis(index='timestamp')

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

        data_dfs = []

        time_series_elements = root.findall('.//ns:TimeSeries', namespace)
        for period in time_series_elements:
            start_date = datetime.strptime(period.find('.//ns:timeInterval/ns:start', namespace).text,
                                           '%Y-%m-%dT%H:%MZ')
            end_date = datetime.strptime(period.find('.//ns:timeInterval/ns:end', namespace).text, '%Y-%m-%dT%H:%MZ')
            resolution = period.find('.//ns:resolution', namespace).text
            interval_minutes = cls._get_resolution_interval(resolution)

            money_unit = period.find('.//ns:currency_Unit.name', namespace).text
            energy_unit = period.find('.//ns:price_Measure_Unit.name', namespace).text

            data_rows = []
            for point in period.findall('.//ns:Point', namespace):
                position = int(point.find('ns:position', namespace).text)
                price = float(point.find('ns:price.amount', namespace).text)

                data_rows.append({
                    'timestamp': start_date + timedelta(minutes=interval_minutes * (position - 1)),
                    'Price': price,
                    'MoneyUnit': money_unit,
                    'EnergyUnit': energy_unit,
                    'resolution': resolution,
                })

            df = pd.DataFrame(data_rows).set_index('timestamp')
            df = cls._fill_gaps(df, interval_minutes, time_start=start_date, time_end=end_date)

            data_dfs.append(df)

        return pd.concat(data_dfs).sort_index()
