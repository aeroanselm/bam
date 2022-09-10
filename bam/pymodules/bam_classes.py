"""
bam_classes module.
Contains the base classes of the project.
"""

import time
from typing import List

from bam.pymodules import ExpenditureEnum, IncomeEnum


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
        self.__type: IncomeEnum | None = None

    def get_type(self) -> IncomeEnum | None:
        """
        get_type self.__type getter method

        :return: self.__type
        :rtype: IncomeEnum
        """
        return self.__type


class Expenditure(Transaction):
    """
    Expenditure class
    Builds an object Transaction.Expenditure
    """

    def __init__(self, value: float) -> None:
        """Constructor method

        :param value: absolute expenditure value without sign
        :type value: float
        """
        super().__init__(value=value)
        self.__type: ExpenditureEnum | None = None

    def get_type(self) -> ExpenditureEnum | None:
        """
        get_type self.__type getter method

        :return: self.__type
        :rtype: ExpenditureEnum
        """
        return self.__type


class Balance:
    """
    Balance class
    Builds an object Balance
    """

    def __init__(self, initial_balance: float = 0.0) -> None:
        self.__balance = initial_balance
        self.__incomes: List[Income] | None = None
        self.__expenditures: List[Expenditure] | None = None

    def __update_balance(self) -> None:
        """
        __update_balance updates balance value permorming an algebric sum
        between incomes and expenditures
        """
        total_income = 0.0
        total_expenditure = 0.0
        if self.__incomes is not None:
            for income in self.__incomes:
                total_income += income.get_value()
        if self.__expenditures is not None:
            for expenditure in self.__expenditures:
                total_expenditure += expenditure.get_value()
        self.__balance = total_income - total_expenditure

    def add_income(self, income: Income) -> None:
        """
        add_income adds an income to the balance list of incomes, then
        ricalculates the balance

        :param income: income to be added to the balance
        :type income: Income
        """
        if self.__incomes is not None:
            self.__incomes.append(income)
        else:
            self.__incomes = [income]
        self.__update_balance()

    def add_expenditure(self, expenditure: Expenditure) -> None:
        """
        add_income adds an expenditure to the balance list of expenditures, then
        ricalculates the balance

        :param expenditure: expenditure to be added to the balance
        :type income: Expenditure
        """
        if self.__expenditures is not None:
            self.__expenditures.append(expenditure)
        else:
            self.__expenditures = [expenditure]
        self.__update_balance()

    def get_balance(self) -> float:
        """
        get_balance self.__balance getter method

        :return: self.__balance
        :rtype: float
        """
        return self.__balance

    # TODO: add method to get the balance inside time range, incomes and
    # expenditures inside time range as well.
