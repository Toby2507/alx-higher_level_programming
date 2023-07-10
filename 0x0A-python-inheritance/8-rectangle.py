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
    """

    def __init__(self, width, height):
        """Initializes the rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
