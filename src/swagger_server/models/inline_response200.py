# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, num: int=None, type: str=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param num: The num of this InlineResponse200.  # noqa: E501
        :type num: int
        :param type: The type of this InlineResponse200.  # noqa: E501
        :type type: str
        """
        self.swagger_types = {
            'num': int,
            'type': str
        }

        self.attribute_map = {
            'num': 'num',
            'type': 'type'
        }

        self._num = num
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def num(self) -> int:
        """Gets the num of this InlineResponse200.


        :return: The num of this InlineResponse200.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num: int):
        """Sets the num of this InlineResponse200.


        :param num: The num of this InlineResponse200.
        :type num: int
        """

        self._num = num

    @property
    def type(self) -> str:
        """Gets the type of this InlineResponse200.


        :return: The type of this InlineResponse200.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this InlineResponse200.


        :param type: The type of this InlineResponse200.
        :type type: str
        """

        self._type = type
