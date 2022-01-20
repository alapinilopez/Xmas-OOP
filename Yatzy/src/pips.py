from enum import Enum, unique, IntEnum
from numbers import Number

@unique
class Pips(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def get_values(cls):
        print(Pips.__members__.values())
        return [number._value_ for number in Pips.__members__.values()]
    @classmethod
    def values_reversed(cls):
        return reversed(cls.get_values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values - {pip.value})

Pips.get_values()