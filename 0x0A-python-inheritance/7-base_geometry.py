#!/usr/bin/python3
"""
Contains an empty class BaseGeometry
"""


class BaseGeometry:
    """A blueprint for BaseGeometry

    Methods:
        area: raises an exception
        integer_validator: validates class input
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates input as an integer greater than 0

        Args:
            name (str): name
            value (int): value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
