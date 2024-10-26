import os
from datetime import datetime, timedelta

from entsoe_api.api import EntsoeAPI
from entsoe_api.enums import DocumentType, ProcessType, DomainType

if __name__ == "__main__":
    # Twój klucz API
    api_key = os.environ.get('ENTSOE_API_KEY')

    # Inicjalizacja API
    entsoe_api = EntsoeAPI(api_key)

    # Okres, dla którego chcesz pobrać dane
    start_date = datetime(2024, 5, 1)
    end_date = datetime(2024, 10, 1) + timedelta(days=1)

    # Pobierz dane o produkcji energii z wiatru (onshore)

    data = entsoe_api.fetch_data(
        start_date=start_date,
        end_date=end_date,
        document_type=DocumentType.ACTUAL_GENERATION_PER_TYPE,
        process_type=ProcessType.REALISED,
        domain=DomainType.DE
    )

    print("done")
