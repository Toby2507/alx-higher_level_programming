#!/usr/bin/python3
"""
Contains a function that returns True if an object is exactly an instance of
the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of a Class

    Args:
        obj: object under review
        a_class: class to be checked

    Returns:
        True if is instance of a_class, False otherwise
    """
    return type(obj) == a_class
