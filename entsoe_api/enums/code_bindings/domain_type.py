from entsoe_api.enums.code_binding import CodeBinding


class DomainType(CodeBinding):
    """
    Enum representing various domain types in the ENTSO-E API.

    Each domain type indicates a specific energy domain within a region or country,
    along with associated codes that represent relevant entities or characteristics.

    Attributes:
        TODO: Add attributes for each domain type with the corresponding code.
    """

    DE = '10Y1001A1001A83F'  # Germany (DE)
    DE2 = '10Y1001A1001A82H'  # Germany (DE) - BZN|DE-LU, IPA|DE-LU, SCA|DE-LU, MBA|DE-LU
