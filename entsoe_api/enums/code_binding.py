from enum import StrEnum

from entsoe_api.enums.exceptions import CodeBindingError


class CodeBinding(StrEnum):
    """
    Interface for the CodeBinding enumeration
    """

    @classmethod
    def from_name(cls, name):
        """Return the corresponding EnumType for a given code.

        Args:
            name (str): The code to search for.

        Returns:
            EnumType: The corresponding EnumType.

        Raises:
            CodeBindingError: If the code is not found.

        """
        try:
            return cls[name]
        except KeyError:
            raise CodeBindingError(
                f"Unknown code '{name}' for {cls.__name__}. Available codes are: {', '.join(cls.__members__)}")
