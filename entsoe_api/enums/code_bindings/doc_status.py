from entsoe_api.enums.code_binding import CodeBinding


class DocStatus(CodeBinding):
    """
    Enum representing the status of a document in the ENTSO-E API.

    The document status indicates the current state of the document,
    whether it is in an intermediate phase, final, or has been cancelled or withdrawn.

    Attributes:
        INTERMEDIATE (str): Intermediate status (code 'A01').
        FINAL (str): Final status (code 'A02').
        ACTIVE (str): Active status (code 'A05').
        CANCELLED (str): Cancelled status (code 'A09').
        WITHDRAWN (str): Withdrawn status (code 'A13').
        ESTIMATED (str): Estimated status (code 'X01').
    """

    INTERMEDIATE = 'A01'
    FINAL = 'A02'
    ACTIVE = 'A05'
    CANCELLED = 'A09'
    WITHDRAWN = 'A13'
    ESTIMATED = 'X01'
