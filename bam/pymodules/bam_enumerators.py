"""
Enumerators library.
Contains all the enum classes of the program.
"""
from enum import Enum


class MonthsEnum(Enum):
    """
    MonthsEnum: months enumerator class
    """    
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


class IncomeEnum(Enum):
    """
    IncomeEnum: Income type enumerator class
    """    
    SALARY = 1
    EXTERNAL_INCOME = 2


class ExpenditureEnum(Enum):
    """
    ExpenditureEnum: Expenditure type enumerator class
    """    
    RENT = 1
    CAR = 2
    HEALTH = 3
    FOOD = 4
    OTHER = 5


class LanguageEnum(Enum):
    """
    LanguageEnum: Language enumerator class
    """    
    ENGLISH = 'en'
    ITALIANO = 'it'


class ColorMenuBgEnum(Enum):
    """
    ColorMenuBgEnum: Menu background color enumerator class
    """    
    BLACK = 'bg_black'
    BLUE = 'bg_blue'
    CYAN = 'bg_cyan'
    GRAY = 'bg_gray'
    GREEN = 'bg_green'
    PURPLE = 'bg_purple'
    RED = 'bg_red'
    YELLOW = 'bg_yellow'


class ColorMenuFgEnum(Enum):
    """
    ColorMenuFgEnum: Menu foreground color enumerator class
    """    
    BLACK = 'fg_black'
    BLUE = 'fg_blue'
    CYAN = 'fg_cyan'
    GRAY = 'fg_gray'
    GREEN = 'fg_green'
    PURPLE = 'fg_purple'
    RED = 'fg_red'
    YELLOW = 'fg_yellow'