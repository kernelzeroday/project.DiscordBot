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

class CourseCreditTransfer(object):
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
        'igetc': 'str',
        'csu': 'str'
    }

    attribute_map = {
        'igetc': 'igetc',
        'csu': 'csu'
    }

    def __init__(self, igetc=None, csu=None):  # noqa: E501
        """CourseCreditTransfer - a model defined in Swagger"""  # noqa: E501
        self._igetc = None
        self._csu = None
        self.discriminator = None
        if igetc is not None:
            self.igetc = igetc
        if csu is not None:
            self.csu = csu

    @property
    def igetc(self):
        """Gets the igetc of this CourseCreditTransfer.  # noqa: E501

        IGETC transfer information text for the course.  # noqa: E501

        :return: The igetc of this CourseCreditTransfer.  # noqa: E501
        :rtype: str
        """
        return self._igetc

    @igetc.setter
    def igetc(self, igetc):
        """Sets the igetc of this CourseCreditTransfer.

        IGETC transfer information text for the course.  # noqa: E501

        :param igetc: The igetc of this CourseCreditTransfer.  # noqa: E501
        :type: str
        """

        self._igetc = igetc

    @property
    def csu(self):
        """Gets the csu of this CourseCreditTransfer.  # noqa: E501

        CSU transfer information text for the course.  # noqa: E501

        :return: The csu of this CourseCreditTransfer.  # noqa: E501
        :rtype: str
        """
        return self._csu

    @csu.setter
    def csu(self, csu):
        """Sets the csu of this CourseCreditTransfer.

        CSU transfer information text for the course.  # noqa: E501

        :param csu: The csu of this CourseCreditTransfer.  # noqa: E501
        :type: str
        """

        self._csu = csu

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
        if issubclass(CourseCreditTransfer, dict):
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
        if not isinstance(other, CourseCreditTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
