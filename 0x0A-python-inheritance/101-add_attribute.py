#!/usr/bin/python3
"""
Contains a function that adds a new attribute to an object if it's possible
"""


def add_attribute(a_class, atrr, value):
    """adds a new attribute to a_class

    Args:
        a_class (class): class
        atrr (str): attribute to be added
        value (string): new value
    """
    if not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a_class, atrr, value)
