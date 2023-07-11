#!/usr/bin/python3
"""
Contains a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Computes the list of available attributes and methods

    Returns:
        list of available attributes and methods
    """
    return dir(obj)
