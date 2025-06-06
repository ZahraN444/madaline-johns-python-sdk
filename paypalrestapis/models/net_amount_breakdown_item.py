# -*- coding: utf-8 -*-

"""
paypalrestapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalrestapis.api_helper import APIHelper
from paypalrestapis.models.exchange_rate import ExchangeRate
from paypalrestapis.models.money import Money


class NetAmountBreakdownItem(object):

    """Implementation of the 'Net Amount Breakdown Item' model.

    The net amount. Returned when the currency of the refund is different from
    the currency of the PayPal account where the merchant holds their funds.

    Attributes:
        payable_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        converted_amount (Money): The currency and amount for a financial
            transaction, such as a balance or payment due.
        exchange_rate (ExchangeRate): The exchange rate that determines the
            amount to convert from one currency to another currency.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payable_amount": 'payable_amount',
        "converted_amount": 'converted_amount',
        "exchange_rate": 'exchange_rate'
    }

    _optionals = [
        'payable_amount',
        'converted_amount',
        'exchange_rate',
    ]

    def __init__(self,
                 payable_amount=APIHelper.SKIP,
                 converted_amount=APIHelper.SKIP,
                 exchange_rate=APIHelper.SKIP):
        """Constructor for the NetAmountBreakdownItem class"""

        # Initialize members of the class
        if payable_amount is not APIHelper.SKIP:
            self.payable_amount = payable_amount 
        if converted_amount is not APIHelper.SKIP:
            self.converted_amount = converted_amount 
        if exchange_rate is not APIHelper.SKIP:
            self.exchange_rate = exchange_rate 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        payable_amount = Money.from_dictionary(dictionary.get('payable_amount')) if 'payable_amount' in dictionary.keys() else APIHelper.SKIP
        converted_amount = Money.from_dictionary(dictionary.get('converted_amount')) if 'converted_amount' in dictionary.keys() else APIHelper.SKIP
        exchange_rate = ExchangeRate.from_dictionary(dictionary.get('exchange_rate')) if 'exchange_rate' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(payable_amount,
                   converted_amount,
                   exchange_rate)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'payable_amount={(self.payable_amount if hasattr(self, "payable_amount") else None)!r}, '
                f'converted_amount={(self.converted_amount if hasattr(self, "converted_amount") else None)!r}, '
                f'exchange_rate={(self.exchange_rate if hasattr(self, "exchange_rate") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'payable_amount={(self.payable_amount if hasattr(self, "payable_amount") else None)!s}, '
                f'converted_amount={(self.converted_amount if hasattr(self, "converted_amount") else None)!s}, '
                f'exchange_rate={(self.exchange_rate if hasattr(self, "exchange_rate") else None)!s})')
