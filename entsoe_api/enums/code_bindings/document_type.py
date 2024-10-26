from entsoe_api.enums.code_binding import CodeBinding


class DocumentType(CodeBinding):
    """
    Enum representing various types of documents used in the ENTSO-E API.

    Each document type corresponds to a specific kind of report or data set that
    can be requested from the ENTSO-E API, such as schedules, forecasts, or availability reports.

    Attributes:
        FINALISED_SCHEDULE (str): Finalised schedule document (code 'A09').
        AGGREGATED_ENERGY_DATA_REPORT (str): Aggregated energy data report (code 'A11').
        ACQUIRING_SYSTEM_OPERATOR_RESERVE_SCHEDULE (str): Reserve schedule for acquiring system operator (code 'A15').
        BID_DOCUMENT (str): Bid document (code 'A24').
        ALLOCATION_RESULT_DOCUMENT (str): Allocation result document (code 'A25').
        CAPACITY_DOCUMENT (str): Capacity document (code 'A26').
        AGREED_CAPACITY (str): Agreed capacity document (code 'A31').
        RESERVE_BID_DOCUMENT (str): Reserve bid document (code 'A37').
        RESERVE_ALLOCATION_RESULT_DOCUMENT (str): Reserve allocation result document (code 'A38').
        PRICE_DOCUMENT (str): Price document (code 'A44').
        ESTIMATED_NET_TRANSFER_CAPACITY (str): Estimated net transfer capacity (code 'A61').
        REDISPATCH_NOTICE (str): Redispatch notice (code 'A63').
        SYSTEM_TOTAL_LOAD (str): System total load document (code 'A65').
        INSTALLED_GENERATION_PER_TYPE (str): Installed generation per type document (code 'A68').
        WIND_AND_SOLAR_FORECAST (str): Wind and solar forecast (code 'A69').
        LOAD_FORECAST_MARGIN (str): Load forecast margin (code 'A70').
        GENERATION_FORECAST (str): Generation forecast (code 'A71').
        RESERVOIR_FILLING_INFORMATION (str): Reservoir filling information (code 'A72').
        ACTUAL_GENERATION (str): Actual generation document (code 'A73').
        WIND_AND_SOLAR_GENERATION (str): Wind and solar generation document (code 'A74').
        ACTUAL_GENERATION_PER_TYPE (str): Actual generation per type document (code 'A75').
        LOAD_UNAVAILABILITY (str): Load unavailability document (code 'A76').
        PRODUCTION_UNAVAILABILITY (str): Production unavailability document (code 'A77').
        TRANSMISSION_UNAVAILABILITY (str): Transmission unavailability document (code 'A78').
        OFFSHORE_GRID_INFRASTRUCTURE_UNAVAILABILITY (str): Offshore grid infrastructure unavailability (code 'A79').
        GENERATION_UNAVAILABILITY (str): Generation unavailability document (code 'A80').
        CONTRACTED_RESERVES (str): Contracted reserves document (code 'A81').
        ACCEPTED_OFFERS (str): Accepted offers document (code 'A82').
        ACTIVATED_BALANCING_QUANTITIES (str): Activated balancing quantities document (code 'A83').
        ACTIVATED_BALANCING_PRICES (str): Activated balancing prices document (code 'A84').
        IMBALANCE_PRICES (str): Imbalance prices document (code 'A85').
        IMBALANCE_VOLUME (str): Imbalance volume document (code 'A86').
        FINANCIAL_SITUATION (str): Financial situation document (code 'A87').
        CROSS_BORDER_BALANCING (str): Cross-border balancing document (code 'A88').
        CONTRACTED_RESERVE_PRICES (str): Contracted reserve prices document (code 'A89').
        INTERCONNECTION_NETWORK_EXPANSION (str): Interconnection network expansion document (code 'A90').
        COUNTER_TRADE_NOTICE (str): Counter trade notice document (code 'A91').
        CONGESTION_COSTS (str): Congestion costs document (code 'A92').
        DC_LINK_CAPACITY (str): DC link capacity document (code 'A93').
        NON_EU_ALLOCATIONS (str): Non-EU allocations document (code 'A94').
        CONFIGURATION_DOCUMENT (str): Configuration document (code 'A95').
        FLOW_BASED_ALLOCATIONS (str): Flow-based allocations document (code 'B11').
        AGGREGATED_NETTED_EXTERNAL_TSO_SCHEDULE_DOCUMENT (str): Aggregated netted external TSO schedule document (code 'B17').
        BID_AVAILABILITY_DOCUMENT (str): Bid availability document (code 'B45').
    """
    FINALISED_SCHEDULE = 'A09'
    AGGREGATED_ENERGY_DATA_REPORT = 'A11'
    ACQUIRING_SYSTEM_OPERATOR_RESERVE_SCHEDULE = 'A15'
    BID_DOCUMENT = 'A24'
    ALLOCATION_RESULT_DOCUMENT = 'A25'
    CAPACITY_DOCUMENT = 'A26'
    AGREED_CAPACITY = 'A31'
    RESERVE_BID_DOCUMENT = 'A37'
    RESERVE_ALLOCATION_RESULT_DOCUMENT = 'A38'
    PRICE_DOCUMENT = 'A44'
    ESTIMATED_NET_TRANSFER_CAPACITY = 'A61'
    REDISPATCH_NOTICE = 'A63'
    SYSTEM_TOTAL_LOAD = 'A65'
    INSTALLED_GENERATION_PER_TYPE = 'A68'
    WIND_AND_SOLAR_FORECAST = 'A69'
    LOAD_FORECAST_MARGIN = 'A70'
    GENERATION_FORECAST = 'A71'
    RESERVOIR_FILLING_INFORMATION = 'A72'
    ACTUAL_GENERATION = 'A73'
    WIND_AND_SOLAR_GENERATION = 'A74'
    ACTUAL_GENERATION_PER_TYPE = 'A75'
    LOAD_UNAVAILABILITY = 'A76'
    PRODUCTION_UNAVAILABILITY = 'A77'
    TRANSMISSION_UNAVAILABILITY = 'A78'
    OFFSHORE_GRID_INFRASTRUCTURE_UNAVAILABILITY = 'A79'
    GENERATION_UNAVAILABILITY = 'A80'
    CONTRACTED_RESERVES = 'A81'
    ACCEPTED_OFFERS = 'A82'
    ACTIVATED_BALANCING_QUANTITIES = 'A83'
    ACTIVATED_BALANCING_PRICES = 'A84'
    IMBALANCE_PRICES = 'A85'
    IMBALANCE_VOLUME = 'A86'
    FINANCIAL_SITUATION = 'A87'
    CROSS_BORDER_BALANCING = 'A88'
    CONTRACTED_RESERVE_PRICES = 'A89'
    INTERCONNECTION_NETWORK_EXPANSION = 'A90'
    COUNTER_TRADE_NOTICE = 'A91'
    CONGESTION_COSTS = 'A92'
    DC_LINK_CAPACITY = 'A93'
    NON_EU_ALLOCATIONS = 'A94'
    CONFIGURATION_DOCUMENT = 'A95'
    FLOW_BASED_ALLOCATIONS = 'B11'
    AGGREGATED_NETTED_EXTERNAL_TSO_SCHEDULE_DOCUMENT = 'B17'
    BID_AVAILABILITY_DOCUMENT = 'B45'
