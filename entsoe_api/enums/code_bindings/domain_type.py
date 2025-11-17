from entsoe_api.enums.code_binding import CodeBinding


class DomainType(CodeBinding):
    """
    Enum representing various domain types in the ENTSO-E API.

    Each domain type indicates a specific energy domain within a region or country,
    along with associated codes that represent relevant entities or characteristics.

    Attributes:
        TODO: Add attributes for each domain type with the corresponding code.
    """

    DE = '10Y1001A1001A82H'  # Germany (DE_LU)
    FR = '10YFR-RTE------C'  # France (FR)
    AT = '10YAT-APG------L'  # Austria (AT)
    BE = '10YBE----------2'  # Belgium (BE)
    CH = '10YCH-SWISSGRIDZ'  # Switzerland (CH)
    CZ = '10YCZ-CEPS-----N'  # Czech Republic (CZ)
    DK1 = '10YDK-1--------W'  # Denmark (DK1)
    DK2 = '10YDK-2--------M'  # Denmark (DK2)
    NL = '10YNL----------L'  # Netherlands (NL)
    NO2 = '10YNO-2--------T'  # Norway (NO2)
    PL = '10YPL-AREA-----S'  # Poland (PL)
    ES = '10YES-REE------0'  # Spain (ES)
    GB = '10YGB----------A'  # Great Britain (GB)
    GB_ElecLink = '11Y0-0000-0265-K'  # ElecLink (GB)
    GB_IFA = '10Y1001C--00098F'  # IFA (GB)
    GB_IFA2 = '17Y0000009369493'  # IFA2 (GB)
    IT_North = '10Y1001A1001A73I'  # Italy North (IT)
    IT_North_FR = '10Y1001A1001A81J'  # Italy North (IT_FR)
    DE_AT_LU = '10Y1001A1001A63L'  # DE-AT-LU (DE_AT_LU)
    IT_Centre_South = '10Y1001A1001A71M'  # Italy Centre-South (IT)
    IT_Centre_North = '10Y1001A1001A70O'  # Italy Centre-North (IT)
    IT_Sardinia = '10Y1001A1001A74G'  # Italy Sardinia (IT)
    IT_South = '10Y1001A1001A788'  # Italy South (IT)
    ME = '10YCS-CG-TSO---S'  # Montenegro (ME)
    CZ_DE_SK = '10YDOM-CZ-DE-SKK'  # CZ-DE-SK (CZ_DE_SK)
    LT = '10YLT-1001A0008Q'  # Lithuania (LT)
    SE4 = '10Y1001A1001A47J'  # Sweden (SE4)
    SK = '10YSK-SEPS-----K'  # Slovakia (SK)
    UA = '10Y1001C--00003F'  # Ukraine (UA)
    UA_DobTPP = '10Y1001A1001A869'  # DobTPP (UA)
    UA_IPS = '10Y1001C--000182'  # IPS (UA)
    NO1 = '10YNO-1--------2'  # Norway (NO1)
    NO2A = '10Y1001C--001219'  # Norway (NO2A)
    NO5 = '10Y1001A1001A48H'  # Norway (NO5)
    NO4 = '10YNO-4--------9'  # Norway (NO4)
    FI = '10YFI-1--------U'  # Finland (FI)
    NO3 = '10YNO-3--------J'  # Norway (NO3)
    SE1 = '10Y1001A1001A44P'  # Sweden (SE1)
    SE2 = '10Y1001A1001A45N'  # Sweden (SE2)