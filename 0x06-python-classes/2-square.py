#!/usr/bin/python3
"""
This module contains a class called Square that defines a square.
It is based on file 1-square.py
"""


class Square:
    """This is a class that defines a square with appropriate warnings"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
