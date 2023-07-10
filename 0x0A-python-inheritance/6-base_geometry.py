#!/usr/bin/python3
"""
Contains an empty class BaseGeometry
"""


class BaseGeometry:
    """A blueprint for BaseGeometry

    Methods:
        area: raises an exception
    """

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")
