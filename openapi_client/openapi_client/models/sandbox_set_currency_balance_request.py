# coding: utf-8

"""
    OpenAPI

    tinkoff.ru/invest OpenAPI.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: n.v.melnikov@tinkoff.ru
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SandboxSetCurrencyBalanceRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'currency': 'SandboxCurrency',
        'balance': 'float'
    }

    attribute_map = {
        'currency': 'currency',
        'balance': 'balance'
    }

    def __init__(self, currency=None, balance=None):  # noqa: E501
        """SandboxSetCurrencyBalanceRequest - a model defined in OpenAPI"""  # noqa: E501

        self._currency = None
        self._balance = None
        self.discriminator = None

        self.currency = currency
        self.balance = balance

    @property
    def currency(self):
        """Gets the currency of this SandboxSetCurrencyBalanceRequest.  # noqa: E501


        :return: The currency of this SandboxSetCurrencyBalanceRequest.  # noqa: E501
        :rtype: SandboxCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SandboxSetCurrencyBalanceRequest.


        :param currency: The currency of this SandboxSetCurrencyBalanceRequest.  # noqa: E501
        :type: SandboxCurrency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def balance(self):
        """Gets the balance of this SandboxSetCurrencyBalanceRequest.  # noqa: E501


        :return: The balance of this SandboxSetCurrencyBalanceRequest.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SandboxSetCurrencyBalanceRequest.


        :param balance: The balance of this SandboxSetCurrencyBalanceRequest.  # noqa: E501
        :type: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SandboxSetCurrencyBalanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
