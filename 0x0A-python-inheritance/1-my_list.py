#!/usr/bin/python3
"""module that contains a class Myclass that inherits from list"""


class MyList(list):
    """class mylist that inherites from list """
    def print_sorted(self):
        """This funtion prints the list but sorted """
        print(sorted(self))
