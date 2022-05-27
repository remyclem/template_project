# codding: utf-8
"""
Template for creating an enum.
"""
from enum_template import Enum


class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


if __name__ == "__main__":

    birthday_month = Month.MARCH
    if birthday_month == Month.MARCH:
        print("Happy Birthday!")