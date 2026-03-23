from entsoe_api.enums.code_binding import CodeBinding


class DomainType(CodeBinding):
    """
    Enum representing various domain types in the ENTSO-E API.

    Each domain type indicates a specific energy domain within a region or country,
    along with associated codes that represent relevant entities or characteristics.
    Note that the codes among the domain types (BZN, CTA, CTY) may have overlapping values.

    Attributes:
        TODO: Add attributes for each domain type with the corresponding code.
    """

    # BZN stands for "Bidding Zone Name" and represents the specific energy market zones within the ENTSO-E framework. Each code corresponds to a particular country or region's bidding zone, which is crucial for energy trading and market operations.
    BZN_AT = '10YAT-APG------L'  # Austria
    BZN_BE = '10YBE----------2'  # Belgium
    BZN_BG = '10YCA-BULGARIA-R'  # Bulgaria
    BZN_CH = '10YCH-SWISSGRIDZ'  # Switzerland
    BZN_CZ = '10YCZ-CEPS-----N'  # Czech Republic
    BZN_DE_LU = '10Y1001A1001A82H'  # DE-LU
    BZN_DK1 = '10YDK-1--------W'  # DK1
    BZN_DK2 = '10YDK-2--------M'  # DK2
    BZN_EE = '10Y1001A1001A39I'  # Estonia
    BZN_ES = '10YES-REE------0'  # Spain
    BZN_FI = '10YFI-1--------U'  # Finland
    BZN_FR = '10YFR-RTE------C'  # France
    BZN_GR = '10YGR-HTSO-----Y'  # Greece
    BZN_HR = '10YHR-HEP------M'  # Croatia
    BZN_HU = '10YHU-MAVIR----U'  # Hungary
    BZN_IE_SEM = '10Y1001A1001A59C'  # IE(SEM)
    BZN_IT_NORTH = '10Y1001A1001A73I'  # IT-North
    BZN_IT_CNORTH = '10Y1001A1001A70O'  # IT-Centre-North
    BZN_IT_CSOUTH = '10Y1001A1001A71M'  # IT-Centre-South
    BZN_IT_SOUTH = '10Y1001A1001A788'  # IT-South
    BZN_IT_Calabria = '10Y1001C--00096J'  # IT-Calabria
    BZN_IT_Sicily = '10Y1001A1001A75E'  # IT-Sicily
    BZN_IT_SACODC = '10Y1001A1001A893'  # IT-SACODC
    BZN_IT_Sardinia = '10Y1001A1001A74G'  # IT-Sardinia
    BZN_IT_SACOAC = '10Y1001A1001A885'  # IT-SACOAC
    BZN_LT = '10YLT-1001A0008Q'  # Lithuania
    BZN_LV = '10YLV-1001A00074'  # Latvia
    BZN_ME = '10YCS-CG-TSO---S'  # Montenegro
    BZN_MK = '10YMK-MEPSO----8'  # North Macedonia
    BZN_NL = '10YNL----------L'  # Netherlands
    BZN_NO1 = '10YNO-1--------2'  # NO1
    BZN_NO2 = '10YNO-2--------T'  # NO2
    BZN_NO5 = '10Y1001A1001A48H'  # NO5
    BZN_NO3 = '10YNO-3--------J'  # NO3
    BZN_NO4 = '10YNO-4--------9'  # NO4
    BZN_PL = '10YPL-AREA-----S'  # Poland
    BZN_PT = '10YPT-REN------W'  # Portugal
    BZN_RO = '10YRO-TEL------P'  # Romania
    BZN_SE4 = '10Y1001A1001A47J'  # SE4
    BZN_SE3 = '10Y1001A1001A46L'  # SE3
    BZN_SE2 = '10Y1001A1001A45N'  # SE2
    BZN_SE1 = '10Y1001A1001A44P'  # SE1
    BZN_SI = '10YSI-ELES-----O'  # Slovenia
    BZN_SK = '10YSK-SEPS-----K'  # Slovakia
    BZN_GB = '10YGB----------A'  # GB
    BZN_TR = '10YTR-TEIAS----W'  # Turkey
    BZN_MT = '10Y1001A1001A93C'  # Malta
    BZN_CY = '10YCY-1001A0003J'  # Cyprus
    BZN_IS = 'IS'  # Iceland
    BZN_AL = '10YAL-KESH-----5'  # Albania
    BZN_BA = '10YBA-JPCC-----D'  # Bosnia and Herz.
    BZN_RS = '10YCS-SERBIATSOV'  # Serbia
    BZN_UA_IPS = '10Y1001C--000182'  # UA-IPS
    BZN_BY = '10Y1001A1001A51S'  # Belarus
    BZN_RU = '10Y1001A1001A49F'  # Russia
    BZN_MD = '10Y1001A1001A990'  # Moldova
    BZN_RU_KGD = '10Y1001A1001A50U'  # RU-KGD
    BZN_GE = '10Y1001A1001B012'  # Georgia
    BZN_AZ = '10Y1001A1001B05V'  # Azerbaijan
    BZN_AM = '10Y1001A1001B004'  # Armenia
    BZN_XK = '10Y1001C--00100H'  # Kosovo
    # CTA stands for "Control Area" and represents the specific control areas within the ENTSO-E framework. Each code corresponds to a particular country or region's control area, which is essential for managing and balancing the electricity grid within that area.
    CTA_AT = '10YAT-APG------L'  # Austria
    CTA_BE = '10YBE----------2'  # Belgium
    CTA_BG = '10YCA-BULGARIA-R'  # Bulgaria
    CTA_CH = '10YCH-SWISSGRIDZ'  # Switzerland
    CTA_CZ = '10YCZ-CEPS-----N'  # Czech Republic
    CTA_DE_TenneT_GER = '10YDE-EON------1'  # DE(TenneT GER)
    CTA_DE_50HzT = '10YDE-VE-------2'  # DE(50Hertz)
    CTA_DE_Amprion = '10YDE-RWENET---I'  # DE(Amprion)
    CTA_DE_TransnetBW = '10YDE-ENBW-----N'  # DE(TransnetBW)
    CTA_DK = '10Y1001A1001A796'  # DK
    CTA_EE = '10Y1001A1001A39I'  # Estonia
    CTA_ES = '10YES-REE------0'  # Spain
    CTA_FI = '10YFI-1--------U'  # Finland
    CTA_FR = '10YFR-RTE------C'  # France
    CTA_GR = '10YGR-HTSO-----Y'  # Greece
    CTA_HR = '10YHR-HEP------M'  # Croatia
    CTA_HU = '10YHU-MAVIR----U'  # Hungary
    CTA_IE = '10YIE-1001A00010'  # Ireland
    CTA_IT = '10YIT-GRTN-----B'  # Italy
    CTA_LT = '10YLT-1001A0008Q'  # Lithuania
    CTA_LU = '10YLU-CEGEDEL-NQ'  # Luxembourg
    CTA_LV = '10YLV-1001A00074'  # Latvia
    CTA_ME = '10YCS-CG-TSO---S'  # Montenegro
    CTA_MK = '10YMK-MEPSO----8'  # North Macedonia
    CTA_NL = '10YNL----------L'  # Netherlands
    CTA_NO = '10YNO-0--------C'  # Norway
    CTA_PL = '10YPL-AREA-----S'  # Poland
    CTA_PT = '10YPT-REN------W'  # Portugal
    CTA_RO = '10YRO-TEL------P'  # Romania
    CTA_SE = '10YSE-1--------K'  # Sweden
    CTA_SI = '10YSI-ELES-----O'  # Slovenia
    CTA_SK = '10YSK-SEPS-----K'  # Slovakia
    CTA_GB = '10YGB----------A'  # GB
    CTA_NIE = '10Y1001A1001A016'  # NIE
    CTA_TR = '10YTR-TEIAS----W'  # Turkey
    CTA_MT = '10Y1001A1001A93C'  # Malta
    CTA_CY = '10YCY-1001A0003J'  # Cyprus
    CTA_IS = 'IS'  # Iceland
    CTA_AL = '10YAL-KESH-----5'  # Albania
    CTA_BA = '10YBA-JPCC-----D'  # Bosnia and Herz.
    CTA_RS = '10YCS-SERBIATSOV'  # Serbia
    CTA_UA_IPS = '10Y1001C--000182'  # UA-IPS
    CTA_BY = '10Y1001A1001A51S'  # Belarus
    CTA_RU = '10Y1001A1001A49F'  # Russia
    CTA_MD = '10Y1001A1001A990'  # Moldova
    CTA_UA_DobTPP = '10Y1001A1001A869'  # UA-DobTPP
    CTA_RU_KGD = '10Y1001A1001A50U'  # RU-KGD
    CTA_GE = '10Y1001A1001B012'  # Georgia
    CTA_AZ = '10Y1001A1001B05V'  # Azerbaijan
    CTA_AM = '10Y1001A1001B004'  # Armenia
    CTA_XK = '10Y1001C--00100H'  # Kosovo
    # CTY stands for "Country" and represents the specific countries within the ENTSO-E framework. Each code corresponds to a particular country, which is important for identifying the geographical scope of energy data and market operations.
    CTY_AL = '10YAL-KESH-----5'  # Albania
    CTY_AT = '10YAT-APG------L'  # Austria
    CTY_BY = '10Y1001A1001A51S'  # Belarus
    CTY_BE = '10YBE----------2'  # Belgium
    CTY_BA = 'CTY|10YBA-JPCC-----D'  # Bosnia and Herz.
    CTY_BG = 'CTY|10YCA-BULGARIA-R'  # Bulgaria
    CTY_HR = '10YHR-HEP------M'  # Croatia
    CTY_CY = '10YCY-1001A0003J'  # Cyprus
    CTY_CZ = '10YCZ-CEPS-----N'  # Czech Republic
    CTY_DK = '10Y1001A1001A65H'  # Denmark
    CTY_EE = '10Y1001A1001A39I'  # Estonia
    CTY_FI = '10YFI-1--------U'  # Finland
    CTY_MK = '10YMK-MEPSO----8'  # North Macedonia
    CTY_FR = '10YFR-RTE------C'  # France
    CTY_GE = '10Y1001A1001B012'  # Georgia
    CTY_DE = '10Y1001A1001A83F'  # Germany
    CTY_GR = '10YGR-HTSO-----Y'  # Greece
    CTY_HU = '10YHU-MAVIR----U'  # Hungary
    CTY_IS = 'IS'  # Iceland
    CTY_IE = '10YIE-1001A00010'  # Ireland
    CTY_IT = '10YIT-GRTN-----B'  # Italy
    CTY_LV = '10YLV-1001A00074'  # Latvia
    CTY_LT = '10YLT-1001A0008Q'  # Lithuania
    CTY_LU = '10YLU-CEGEDEL-NQ'  # Luxembourg
    CTY_MT = '10Y1001A1001A93C'  # Malta
    CTY_ME = '10YCS-CG-TSO---S'  # Montenegro
    CTY_NL = '10YNL----------L'  # Netherlands
    CTY_NO = '10YNO-0--------C'  # Norway
    CTY_PL = '10YPL-AREA-----S'  # Poland
    CTY_PT = '10YPT-REN------W'  # Portugal
    CTY_MD = '10Y1001A1001A990'  # Moldova
    CTY_RO = '10YRO-TEL------P'  # Romania
    CTY_RU = '10Y1001A1001A49F'  # Russia
    CTY_SK = '10YSK-SEPS-----K'  # Slovakia
    CTY_SI = '10YSI-ELES-----O'  # Slovenia
    CTY_ES = '10YES-REE------0'  # Spain
    CTY_SE = '10YSE-1--------K'  # Sweden
    CTY_CH = '10YCH-SWISSGRIDZ'  # Switzerland
    CTY_TR = '10YTR-TEIAS----W'  # Turkey
    CTY_UA = '10Y1001C--00003F'  # Ukraine
    CTY_UK = '10Y1001A1001A92E'  # United Kingdom
    CTY_AM = '10Y1001A1001B004'  # Armenia
    CTY_AZ = '10Y1001A1001B05V'  # Azerbaijan
    CTY_RS = '10YCS-SERBIATSOV'  # Serbia
    CTY_XK = '10Y1001C--00100H'  # Kosovo