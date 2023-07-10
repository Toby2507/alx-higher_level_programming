#!/usr/bin/python3
"""
Contains a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """checks if obj is a class or subclass of a_class

    Args:
        obj: object
        a_class: class
    Returns:
        True on success, False otherwise
    """
    return isinstance(obj, a_class)
