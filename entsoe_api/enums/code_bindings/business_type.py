from entsoe_api.enums.code_binding import CodeBinding


class BusinessType(CodeBinding):
    """
    Enum representing various types of business processes in the ENTSO-E API.

    Each business type indicates a specific kind of operation or
    data related to energy production and consumption.

    Attributes:
        PRODUCTION (str): Production business type (code 'A01').
        CONSUMPTION (str): Consumption business type (code 'A04').
        AGGREGATED_ENERGY_DATA (str): Aggregated energy data (code 'A14').
        BALANCE_ENERGY_DEVIATION (str): Balance energy deviation (code 'A19').
        GENERAL_CAPACITY_INFORMATION (str): General capacity information (code 'A25').
        ALREADY_ALLOCATED_CAPACITY_AAC (str): Already allocated capacity (AAC) (code 'A29').
        INSTALLED_GENERATION (str): Installed generation (code 'A37').
        REQUESTED_CAPACITY_WITHOUT_PRICE (str): Requested capacity without price (code 'A43').
        SYSTEM_OPERATOR_REDISPATCHING (str): System operator redispatching (code 'A46').
        PLANNED_MAINTENANCE (str): Planned maintenance (code 'A53').
        UNPLANNED_OUTAGE (str): Unplanned outage (code 'A54').
        MINIMUM_POSSIBLE (str): Minimum possible capacity (code 'A60').
        MAXIMUM_POSSIBLE (str): Maximum possible capacity (code 'A61').
        INTERNAL_REDISPATCH (str): Internal redispatch (code 'A85').
        POSITIVE_FORECAST_MARGIN (str): Positive forecast margin (code 'A91').
        NEGATIVE_FORECAST_MARGIN (str): Negative forecast margin (code 'A92').
        WIND_GENERATION (str): Wind generation (code 'A93').
        SOLAR_GENERATION (str): Solar generation (code 'A94').
        FREQUENCY_CONTAINMENT_RESERVE (str): Frequency containment reserve (code 'A95').
        AUTOMATIC_FREQUENCY_RESTORATION_RESERVE (str): Automatic frequency restoration reserve (code 'A96').
        MANUAL_FREQUENCY_RESTORATION_RESERVE (str): Manual frequency restoration reserve (code 'A97').
        REPLACEMENT_RESERVE (str): Replacement reserve (code 'A98').
        INTERCONNECTOR_NETWORK_EVOLUTION (str): Interconnector network evolution (code 'B01').
        INTERCONNECTOR_NETWORK_DISMANTLING (str): Interconnector network dismantling (code 'B02').
        COUNTER_TRADE (str): Counter trade (code 'B03').
        CONGESTION_COSTS (str): Congestion costs (code 'B04').
        CAPACITY_ALLOCATED_WITH_PRICE (str): Capacity allocated with price (code 'B05').
        AUCTION_REVENUE (str): Auction revenue (code 'B07').
        TOTAL_NOMINATED_CAPACITY (str): Total nominated capacity (code 'B08').
        NET_POSITION (str): Net position (code 'B09').
        CONGESTION_INCOME (str): Congestion income (code 'B10').
        PRODUCTION_UNIT (str): Production unit (code 'B11').
        AREA_CONTROL_ERROR (str): Area control error (code 'B33').
        OFFER (str): Offer (code 'B74').
        NEED (str): Need (code 'B75').
        PROCURED_CAPACITY (str): Procured capacity (code 'B95').
        SHARED_BALANCING_RESERVE_CAPACITY (str): Shared balancing reserve capacity (code 'C22').
        SHARE_OF_RESERVE_CAPACITY (str): Share of reserve capacity (code 'C23').
        ACTUAL_RESERVE_CAPACITY (str): Actual reserve capacity (code 'C24').
    """
    PRODUCTION = 'A01'
    CONSUMPTION = 'A04'
    AGGREGATED_ENERGY_DATA = 'A14'
    BALANCE_ENERGY_DEVIATION = 'A19'
    GENERAL_CAPACITY_INFORMATION = 'A25'
    ALREADY_ALLOCATED_CAPACITY_AAC = 'A29'
    INSTALLED_GENERATION = 'A37'
    REQUESTED_CAPACITY_WITHOUT_PRICE = 'A43'
    SYSTEM_OPERATOR_REDISPATCHING = 'A46'
    PLANNED_MAINTENANCE = 'A53'
    UNPLANNED_OUTAGE = 'A54'
    MINIMUM_POSSIBLE = 'A60'
    MAXIMUM_POSSIBLE = 'A61'
    INTERNAL_REDISPATCH = 'A85'
    POSITIVE_FORECAST_MARGIN = 'A91'
    NEGATIVE_FORECAST_MARGIN = 'A92'
    WIND_GENERATION = 'A93'
    SOLAR_GENERATION = 'A94'
    FREQUENCY_CONTAINMENT_RESERVE = 'A95'
    AUTOMATIC_FREQUENCY_RESTORATION_RESERVE = 'A96'
    MANUAL_FREQUENCY_RESTORATION_RESERVE = 'A97'
    REPLACEMENT_RESERVE = 'A98'
    INTERCONNECTOR_NETWORK_EVOLUTION = 'B01'
    INTERCONNECTOR_NETWORK_DISMANTLING = 'B02'
    COUNTER_TRADE = 'B03'
    CONGESTION_COSTS = 'B04'
    CAPACITY_ALLOCATED_WITH_PRICE = 'B05'
    AUCTION_REVENUE = 'B07'
    TOTAL_NOMINATED_CAPACITY = 'B08'
    NET_POSITION = 'B09'
    CONGESTION_INCOME = 'B10'
    PRODUCTION_UNIT = 'B11'
    AREA_CONTROL_ERROR = 'B33'
    OFFER = 'B74'
    NEED = 'B75'
    PROCURED_CAPACITY = 'B95'
    SHARED_BALANCING_RESERVE_CAPACITY = 'C22'
    SHARE_OF_RESERVE_CAPACITY = 'C23'
    ACTUAL_RESERVE_CAPACITY = 'C24'
