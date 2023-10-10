#!/usr/bin/python3
"""module that creates the class MyInt"""


class MyInt(int):
    """
    MyInt class that inherits from the int class
    and reverse the equality and inequality of it
    """

    def __eq__(self, other):
        """ reverse equality into non equality """
        return super().__ne__(other)

    def __ne__(self, other):
        """ reverse non equality into equality """
        return super().__eq__(other)
