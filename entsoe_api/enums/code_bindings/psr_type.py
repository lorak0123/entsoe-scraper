from entsoe_api.enums.code_binding import CodeBinding


class PsrType(CodeBinding):
    """Enum representing various types of production and load sources in the energy sector.

    Each production source type indicates a specific category of energy
    generation or load that can be utilized for reporting and management
    purposes.

    Attributes:
        MIXED (str): Mixed production type (code 'A03').
        GENERATION (str): Generation type (code 'A04').
        LOAD (str): Load type (code 'A05').
        BIOMASS (str): Biomass production type (code 'B01').
        FOSSIL_BROWN_COAL_LIGNITE (str): Fossil brown coal/lignite type (code 'B02').
        FOSSIL_COAL_DERIVED_GAS (str): Fossil coal-derived gas type (code 'B03').
        FOSSIL_GAS (str): Fossil gas type (code 'B04').
        FOSSIL_HARD_COAL (str): Fossil hard coal type (code 'B05').
        FOSSIL_OIL (str): Fossil oil type (code 'B06').
        FOSSIL_OIL_SHALE (str): Fossil oil shale type (code 'B07').
        FOSSIL_PEAT (str): Fossil peat type (code 'B08').
        GEOTHERMAL (str): Geothermal production type (code 'B09').
        HYDRO_PUMPED_STORAGE (str): Hydro pumped storage type (code 'B10').
        HYDRO_RUN_OF_RIVER_POUNDAGE (str): Hydro run-of-river and poundage type (code 'B11').
        HYDRO_WATER_RESERVOIR (str): Hydro water reservoir type (code 'B12').
        MARINE (str): Marine energy type (code 'B13').
        NUCLEAR (str): Nuclear energy type (code 'B14').
        OTHER_RENEWABLE (str): Other renewable energy type (code 'B15').
        SOLAR (str): Solar energy type (code 'B16').
        WASTE (str): Waste energy type (code 'B17').
        WIND_OFFSHORE (str): Offshore wind energy type (code 'B18').
        WIND_ONSHORE (str): Onshore wind energy type (code 'B19').
        OTHER (str): Other unspecified energy types (code 'B20').
        AC_LINK (str): AC link type (code 'B21').
        DC_LINK (str): DC link type (code 'B22').
        SUBSTATION (str): Substation type (code 'B23').
        TRANSFORMER (str): Transformer type (code 'B24').
        ALL (str): All types of energy (code 'ALL').
    """

    MIXED = 'A03'
    GENERATION = 'A04'
    LOAD = 'A05'
    BIOMASS = 'B01'
    FOSSIL_BROWN_COAL_LIGNITE = 'B02'
    FOSSIL_COAL_DERIVED_GAS = 'B03'
    FOSSIL_GAS = 'B04'
    FOSSIL_HARD_COAL = 'B05'
    FOSSIL_OIL = 'B06'
    FOSSIL_OIL_SHALE = 'B07'
    FOSSIL_PEAT = 'B08'
    GEOTHERMAL = 'B09'
    HYDRO_PUMPED_STORAGE = 'B10'
    HYDRO_RUN_OF_RIVER_POUNDAGE = 'B11'
    HYDRO_WATER_RESERVOIR = 'B12'
    MARINE = 'B13'
    NUCLEAR = 'B14'
    OTHER_RENEWABLE = 'B15'
    SOLAR = 'B16'
    WASTE = 'B17'
    WIND_OFFSHORE = 'B18'
    WIND_ONSHORE = 'B19'
    OTHER = 'B20'
    AC_LINK = 'B21'
    DC_LINK = 'B22'
    SUBSTATION = 'B23'
    TRANSFORMER = 'B24'
    ALL = 'ALL'
