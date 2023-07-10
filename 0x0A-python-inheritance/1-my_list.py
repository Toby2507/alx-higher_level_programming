#!/usr/bin/python3
"""
Contains class MyList that inherits from list
"""


class MyList(list):
    """MyList subclass of list"""

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
