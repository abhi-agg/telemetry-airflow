"""
Module with Airflow tag definitions
"""

from enum import Enum


class InvalidTagError(AttributeError):
    pass

class Tag(Enum):
    """
    Enum containing available Airflow tags
    """

    def __getattr__(self, item: str) -> str:
        """
        This is to simplify accessing enum values.
        Instead of Tag.ImpactTier.value.tier_1.value we can just use
        Tag.ImpactTier.tier_1

        # source: https://newbedev.com/enum-of-enums-in-python
        """

        if item == '_value_':
            raise InvalidTagError

        try:
            ret_val = getattr(self.value, item).value
        except AttributeError as _err:
            raise InvalidTagError(_err)

        return ret_val


    class ImpactTier(Enum):
        """
        Valid options for Impact tier tag
        """

        tier_1: str = "impact/tier_1"
        tier_2: str = "impact/tier_2"
        tier_3: str = "impact/tier_3"

    class Triage(Enum):
        """
        Tag for representing that an engineer on triage
        should attempt to resolve the problem themselves
        """

        record_only: str = "triage/record_only"
        no_triage: str = "triage/no_triage"
