#!/usr/bin/python3
"""
Contains a class MyInt that inherits from the int class
"""


class MyInt(int):
    """MyInt blueprint"""

    def __eq__(self, other):
        """override == operator with != behaviour"""
        return self.real != other

    def __ne__(self, other):
        """override != operator with == behaviour"""
        return self.real == other
