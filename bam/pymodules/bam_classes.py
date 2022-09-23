"""
bam_classes module.
Contains the base classes of the project.
"""

import time
from typing import Any, List

import matplotlib as mpl
import matplotlib.pyplot as plt
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
        self.__id: str = ""
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
        self.__type: str = ""

    def get_type(self) -> str:
        """
        get_type self.__type getter method

        :return: self.__type
        :rtype: str
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
        self.__type: str = ""

    def get_type(self) -> str:
        """
        get_type self.__type getter method

        :return: self.__type
        :rtype: str
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

    def remove_income(self, transaction_id: str) -> None:
        """
        remove_income search and remove the income with a prescribed id

        :param transaction_id: income specific id
        :type transaction_id: str
        """
        if self.__incomes is not None:
            for item in self.__incomes:
                if item.get_id() == transaction_id:
                    del item
                    break

    def remove_expenditure(self, transaction_id: str) -> None:
        """
        remove_expenditure search and remove the income with a prescribed id

        :param transaction_id: expenditure specific id
        :type transaction_id: str
        """
        if self.__expenditures is not None:
            for item in self.__expenditures:
                if item.get_id() == transaction_id:
                    del item
                    break

    def get_income(self, transaction_id: str) -> None | Income:
        """
        get_income get income with specific transaction id

        :param transaction_id: transaction id
        :type transaction_id: str
        :return: income item
        :rtype: None | Income
        """
        if self.__incomes is not None:
            for item in self.__incomes:
                if item.get_id() == transaction_id:
                    return item
            return None
        return None

    def get_expenditure(self, transaction_id: str) -> None | Expenditure:
        """
        get_expenditure get expenditure with specific transaction id

        :param transaction_id: transaction id
        :type transaction_id: str
        :return: expenditure item
        :rtype: None | Expenditure
        """
        if self.__expenditures is not None:
            for item in self.__expenditures:
                if item.get_id() == transaction_id:
                    return item
            return None
        return None

    def get_expenditures_list(self) -> List[Expenditure] | None:
        """
        get_expenditures_list getter method for self.__expenditures

        :return: get balance expenditures list
        :rtype: List[Expenditure] | None
        """
        return self.__expenditures

    def get_incomes_list(self) -> List[Income] | None:
        """
        get_incomes_list getter method for self.__incomes

        :return: get balance incomes list
        :rtype: List[Income] | None
        """
        return self.__incomes


class BankAccount:
    """
    BankAccount class
    Builds an objecet BankAccount
    """

    def __init__(self, name: str = "DefaultBankAccount") -> None:
        """
        __init__ Constructor

        :param name: bank account name, defaults to "DefaultBankAccount"
        :type name: str, optional
        """
        self.__name = name
        self.__balance: Balance = Balance()

    def get_name(self) -> str:
        """
        get_name self.__name getter method

        :return: bank account name
        :rtype: str
        """
        return self.__name

    def get_balance(self) -> Balance:
        """
        get_balance self.__balance getter method

        :return: bank account balance
        :rtype: Balance
        """
        return self.__balance

    def set_balance(self, balance: Balance) -> None:
        """
        set_balance self.__balance setter method

        :param balance: set bank account balance
        :type balance: Balance
        """
        self.__balance = balance

    def save_data_to_json(self) -> None:

        # Extracting Incomes and Expenditures lists
        expenditures = self.__balance.get_expenditures_list()
        incomes = self.__balance.get_incomes_list()

        # Saving Transactions as json format
        expenditure_dict = expenditures.__dict__
        income_dict = incomes.__dict__


# class BalanceGraphs:
#     """
#     BalanceGrpahs class
#     Builds an object BalanceClass
#     """
#     # TODO: create grapsh

#     def __init__(self, balance: Balance) -> None:
#         self.__balance = balance
