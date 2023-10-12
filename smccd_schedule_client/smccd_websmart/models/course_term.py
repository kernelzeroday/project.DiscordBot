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

class CourseTerm(object):
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
        'term_code': 'str',
        'term_desc': 'str',
        'part_of_term': 'CourseTermPartOfTerm'
    }

    attribute_map = {
        'term_code': 'term_code',
        'term_desc': 'term_desc',
        'part_of_term': 'part_of_term'
    }

    def __init__(self, term_code=None, term_desc=None, part_of_term=None):  # noqa: E501
        """CourseTerm - a model defined in Swagger"""  # noqa: E501
        self._term_code = None
        self._term_desc = None
        self._part_of_term = None
        self.discriminator = None
        if term_code is not None:
            self.term_code = term_code
        if term_desc is not None:
            self.term_desc = term_desc
        if part_of_term is not None:
            self.part_of_term = part_of_term

    @property
    def term_code(self):
        """Gets the term_code of this CourseTerm.  # noqa: E501

        Term Code of a course.  # noqa: E501

        :return: The term_code of this CourseTerm.  # noqa: E501
        :rtype: str
        """
        return self._term_code

    @term_code.setter
    def term_code(self, term_code):
        """Sets the term_code of this CourseTerm.

        Term Code of a course.  # noqa: E501

        :param term_code: The term_code of this CourseTerm.  # noqa: E501
        :type: str
        """

        self._term_code = term_code

    @property
    def term_desc(self):
        """Gets the term_desc of this CourseTerm.  # noqa: E501

        Term Description.  # noqa: E501

        :return: The term_desc of this CourseTerm.  # noqa: E501
        :rtype: str
        """
        return self._term_desc

    @term_desc.setter
    def term_desc(self, term_desc):
        """Sets the term_desc of this CourseTerm.

        Term Description.  # noqa: E501

        :param term_desc: The term_desc of this CourseTerm.  # noqa: E501
        :type: str
        """

        self._term_desc = term_desc

    @property
    def part_of_term(self):
        """Gets the part_of_term of this CourseTerm.  # noqa: E501


        :return: The part_of_term of this CourseTerm.  # noqa: E501
        :rtype: CourseTermPartOfTerm
        """
        return self._part_of_term

    @part_of_term.setter
    def part_of_term(self, part_of_term):
        """Sets the part_of_term of this CourseTerm.


        :param part_of_term: The part_of_term of this CourseTerm.  # noqa: E501
        :type: CourseTermPartOfTerm
        """

        self._part_of_term = part_of_term

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
        if issubclass(CourseTerm, dict):
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
        if not isinstance(other, CourseTerm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
