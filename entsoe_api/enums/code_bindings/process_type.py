from entsoe_api.enums.code_binding import CodeBinding


class ProcessType(CodeBinding):
    """
    Enum representing various types of processes in the ENTSO-E API.

    Each process type indicates a specific kind of operation related
    to energy management, such as scheduling or balancing reserves.

    Attributes:
        DAY_AHEAD (str): Day ahead process (code 'A01').
        INTRA_DAY_INCREMENTAL (str): Intra-day incremental process (code 'A02').
        REALISED (str): Realised process (code 'A16').
        INTRADAY_TOTAL (str): Intraday total process (code 'A18').
        WEEK_AHEAD (str): Week ahead process (code 'A31').
        MONTH_AHEAD (str): Month ahead process (code 'A32').
        YEAR_AHEAD (str): Year ahead process (code 'A33').
        SYNCHRONISATION_PROCESS (str): Synchronisation process (code 'A39').
        INTRADAY_PROCESS (str): Intraday process (code 'A40').
        REPLACEMENT_RESERVE (str): Replacement reserve process (code 'A46').
        MANUAL_FREQUENCY_RESTORATION_RESERVE (str): Manual frequency restoration reserve process (code 'A47').
        AUTOMATIC_FREQUENCY_RESTORATION_RESERVE (str): Automatic frequency restoration reserve process (code 'A51').
        FREQUENCY_CONTAINMENT_RESERVE (str): Frequency containment reserve process (code 'A52').
        FREQUENCY_RESTORATION_RESERVE (str): Frequency restoration reserve process (code 'A56').
        SCHEDULED_ACTIVATION_MFRR (str): Scheduled activation mFRR process (code 'A60').
        DIRECT_ACTIVATION_MFRR (str): Direct activation mFRR process (code 'A61').
        CENTRAL_SELECTION_AFRR (str): Central selection aFRR process (code 'A67').
        LOCAL_SELECTION_AFRR (str): Local selection aFRR process (code 'A68').
    """
    DAY_AHEAD = 'A01'
    INTRA_DAY_INCREMENTAL = 'A02'
    REALISED = 'A16'
    INTRADAY_TOTAL = 'A18'
    WEEK_AHEAD = 'A31'
    MONTH_AHEAD = 'A32'
    YEAR_AHEAD = 'A33'
    SYNCHRONISATION_PROCESS = 'A39'
    INTRADAY_PROCESS = 'A40'
    REPLACEMENT_RESERVE = 'A46'
    MANUAL_FREQUENCY_RESTORATION_RESERVE = 'A47'
    AUTOMATIC_FREQUENCY_RESTORATION_RESERVE = 'A51'
    FREQUENCY_CONTAINMENT_RESERVE = 'A52'
    FREQUENCY_RESTORATION_RESERVE = 'A56'
    SCHEDULED_ACTIVATION_MFRR = 'A60'
    DIRECT_ACTIVATION_MFRR = 'A61'
    CENTRAL_SELECTION_AFRR = 'A67'
    LOCAL_SELECTION_AFRR = 'A68'
