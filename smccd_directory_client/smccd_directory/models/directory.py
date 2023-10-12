# coding: utf-8

"""
    SMCCD Directory API

    This is SMCCD Directory API documentation. The API requires basic authentication username and password pair to access the data.  # noqa: E501

    OpenAPI spec version: v1.1
    Contact: apiteam@smccd.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Directory(object):
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
        'full_name': 'str',
        'display_name': 'str',
        'given_name': 'str',
        'family_name': 'str',
        'title': 'str',
        'department': 'str',
        'division': 'str',
        'company': 'str',
        'profile_image': 'DirectoryProfileImage',
        'phone': 'str',
        'email': 'str',
        'address': 'DirectoryAddress',
        'links': 'DirectoryLinks'
    }

    attribute_map = {
        'full_name': 'full_name',
        'display_name': 'display_name',
        'given_name': 'given_name',
        'family_name': 'family_name',
        'title': 'title',
        'department': 'department',
        'division': 'division',
        'company': 'company',
        'profile_image': 'profile_image',
        'phone': 'phone',
        'email': 'email',
        'address': 'address',
        'links': '_links'
    }

    def __init__(self, full_name=None, display_name=None, given_name=None, family_name=None, title=None, department=None, division=None, company=None, profile_image=None, phone=None, email=None, address=None, links=None):  # noqa: E501
        """Directory - a model defined in Swagger"""  # noqa: E501
        self._full_name = None
        self._display_name = None
        self._given_name = None
        self._family_name = None
        self._title = None
        self._department = None
        self._division = None
        self._company = None
        self._profile_image = None
        self._phone = None
        self._email = None
        self._address = None
        self._links = None
        self.discriminator = None
        if full_name is not None:
            self.full_name = full_name
        if display_name is not None:
            self.display_name = display_name
        if given_name is not None:
            self.given_name = given_name
        if family_name is not None:
            self.family_name = family_name
        if title is not None:
            self.title = title
        if department is not None:
            self.department = department
        if division is not None:
            self.division = division
        if company is not None:
            self.company = company
        if profile_image is not None:
            self.profile_image = profile_image
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        if address is not None:
            self.address = address
        if links is not None:
            self.links = links

    @property
    def full_name(self):
        """Gets the full_name of this Directory.  # noqa: E501


        :return: The full_name of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this Directory.


        :param full_name: The full_name of this Directory.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def display_name(self):
        """Gets the display_name of this Directory.  # noqa: E501


        :return: The display_name of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Directory.


        :param display_name: The display_name of this Directory.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def given_name(self):
        """Gets the given_name of this Directory.  # noqa: E501


        :return: The given_name of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this Directory.


        :param given_name: The given_name of this Directory.  # noqa: E501
        :type: str
        """

        self._given_name = given_name

    @property
    def family_name(self):
        """Gets the family_name of this Directory.  # noqa: E501


        :return: The family_name of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this Directory.


        :param family_name: The family_name of this Directory.  # noqa: E501
        :type: str
        """

        self._family_name = family_name

    @property
    def title(self):
        """Gets the title of this Directory.  # noqa: E501

        Position title of the person  # noqa: E501

        :return: The title of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Directory.

        Position title of the person  # noqa: E501

        :param title: The title of this Directory.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def department(self):
        """Gets the department of this Directory.  # noqa: E501


        :return: The department of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """Sets the department of this Directory.


        :param department: The department of this Directory.  # noqa: E501
        :type: str
        """

        self._department = department

    @property
    def division(self):
        """Gets the division of this Directory.  # noqa: E501


        :return: The division of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._division

    @division.setter
    def division(self, division):
        """Sets the division of this Directory.


        :param division: The division of this Directory.  # noqa: E501
        :type: str
        """

        self._division = division

    @property
    def company(self):
        """Gets the company of this Directory.  # noqa: E501


        :return: The company of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Directory.


        :param company: The company of this Directory.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def profile_image(self):
        """Gets the profile_image of this Directory.  # noqa: E501


        :return: The profile_image of this Directory.  # noqa: E501
        :rtype: DirectoryProfileImage
        """
        return self._profile_image

    @profile_image.setter
    def profile_image(self, profile_image):
        """Sets the profile_image of this Directory.


        :param profile_image: The profile_image of this Directory.  # noqa: E501
        :type: DirectoryProfileImage
        """

        self._profile_image = profile_image

    @property
    def phone(self):
        """Gets the phone of this Directory.  # noqa: E501


        :return: The phone of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Directory.


        :param phone: The phone of this Directory.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Directory.  # noqa: E501


        :return: The email of this Directory.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Directory.


        :param email: The email of this Directory.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def address(self):
        """Gets the address of this Directory.  # noqa: E501


        :return: The address of this Directory.  # noqa: E501
        :rtype: DirectoryAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Directory.


        :param address: The address of this Directory.  # noqa: E501
        :type: DirectoryAddress
        """

        self._address = address

    @property
    def links(self):
        """Gets the links of this Directory.  # noqa: E501


        :return: The links of this Directory.  # noqa: E501
        :rtype: DirectoryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Directory.


        :param links: The links of this Directory.  # noqa: E501
        :type: DirectoryLinks
        """

        self._links = links

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
        if issubclass(Directory, dict):
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
        if not isinstance(other, Directory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
