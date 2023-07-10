#!/usr/bin/python3
"""
Contains a function that returns True if the object is an instance
of a class that inherited (directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a subclass of a_class

    Args:
        obj: object
        a_class: class

    Returns:
        True on success, False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
