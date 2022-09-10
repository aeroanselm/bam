"""
bam_classes module.
Contains the base classes of the project.
"""

import time

from bam_enumerators import IncomeEnum


class Transaction:
    """
     Transaction class
     Builds an object Transaction
    """

    def __init__(self, value: float) -> None:
        """
        __init__ Constructor

        :param value: transaction value
        :type value: float
        """
        self.__value = value
        self.__description = ""
        self.__subscription = False
        self.__id = ""
        self.__assign_id()

    def __assign_id(self) -> None:
        """
        __assign_id private method to assign the transaction id
        """
        self.__id = hex(time.time_ns())

    def get_id(self) -> str:
        """
        get_id self.__id getter method

        :return: self.__id
        :rtype: str
        """
        return self.__id

    def get_value(self) -> float:
        """
        get_value self.value getter method

        :return: self.__value
        :rtype: float
        """
        return self.__value

    def set_description(self, description: str) -> None:
        """
        set_description self.__description setter method

        :param description: transaction description
        :type description: str
        """
        self.__description = description

    def get_description(self) -> str:
        """
        get_description self.__description getter method

        :return: self.__description
        :rtype: str
        """
        return self.__description

    def set_subscription(self, subscription_flag: bool) -> None:
        """
        set_subscription self.__subscription setter method

        :param subscription_flag: set transaction subscription type
        :type subscription_flag: bool
        """
        self.__subscription = subscription_flag

    def get_subscription(self) -> bool:
        """
        get_subscription self.__subscription getter method

        :return: self.__subscription
        :rtype: bool
        """
        return self.__subscription


class Income(Transaction):
    """
    Income class
    Builds an object Transaction.Income
    """

    def __init__(self, value: float) -> None:
        """Constructor method

        :param value: absolute income value without sign 
        :type value: float
        """
        super().__init__(value=value)
        self.__type: IncomeEnum = IncomeEnum.EXTERNAL_INCOME

    def get_type(self) -> IncomeEnum:
        """
        get_type self.__type getter method

        :return: self.__type
        :rtype: IncomeEnum
        """
        return self.__type
