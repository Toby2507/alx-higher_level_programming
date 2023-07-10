#!/usr/bin/python3
"""
Contains a class Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle blueeprint

    Attributes:
        width (int): reactangle's width
        height (int): rectangle's height

    Methods:
                area: computes the area of the rectangle
    """

    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def __str__(self):
        """should return an unofficial string representation"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """computes the area of the rectangle"""
        return self.__height * self.__width
