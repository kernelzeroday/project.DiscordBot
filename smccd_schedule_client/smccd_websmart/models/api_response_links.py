# coding: utf-8

"""
    SMCCD Schedule API

    This is SMCCD Schedule API documentation. The API requires basic authentication username and password pair to access the data.  # noqa: E501

    OpenAPI spec version: v1
    Contact: webmaster@smccd.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ApiResponseLinks(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        '_self': 'ApiResponseLinksSelf',
        'first': 'CourseLinksSelf',
        'prev': 'CourseLinksSelf',
        'next': 'ApiResponseLinksNext',
        'last': 'ApiResponseLinksLast'
    }

    attribute_map = {
        '_self': 'self',
        'first': 'first',
        'prev': 'prev',
        'next': 'next',
        'last': 'last'
    }

    def __init__(self, _self=None, first=None, prev=None, next=None, last=None):  # noqa: E501
        """ApiResponseLinks - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._first = None
        self._prev = None
        self._next = None
        self._last = None
        self.discriminator = None
        if _self is not None:
            self._self = _self
        if first is not None:
            self.first = first
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next
        if last is not None:
            self.last = last

    @property
    def _self(self):
        """Gets the _self of this ApiResponseLinks.  # noqa: E501


        :return: The _self of this ApiResponseLinks.  # noqa: E501
        :rtype: ApiResponseLinksSelf
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this ApiResponseLinks.


        :param _self: The _self of this ApiResponseLinks.  # noqa: E501
        :type: ApiResponseLinksSelf
        """

        self.__self = _self

    @property
    def first(self):
        """Gets the first of this ApiResponseLinks.  # noqa: E501


        :return: The first of this ApiResponseLinks.  # noqa: E501
        :rtype: CourseLinksSelf
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this ApiResponseLinks.


        :param first: The first of this ApiResponseLinks.  # noqa: E501
        :type: CourseLinksSelf
        """

        self._first = first

    @property
    def prev(self):
        """Gets the prev of this ApiResponseLinks.  # noqa: E501


        :return: The prev of this ApiResponseLinks.  # noqa: E501
        :rtype: CourseLinksSelf
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this ApiResponseLinks.


        :param prev: The prev of this ApiResponseLinks.  # noqa: E501
        :type: CourseLinksSelf
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this ApiResponseLinks.  # noqa: E501


        :return: The next of this ApiResponseLinks.  # noqa: E501
        :rtype: ApiResponseLinksNext
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this ApiResponseLinks.


        :param next: The next of this ApiResponseLinks.  # noqa: E501
        :type: ApiResponseLinksNext
        """

        self._next = next

    @property
    def last(self):
        """Gets the last of this ApiResponseLinks.  # noqa: E501


        :return: The last of this ApiResponseLinks.  # noqa: E501
        :rtype: ApiResponseLinksLast
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this ApiResponseLinks.


        :param last: The last of this ApiResponseLinks.  # noqa: E501
        :type: ApiResponseLinksLast
        """

        self._last = last

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiResponseLinks, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiResponseLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
