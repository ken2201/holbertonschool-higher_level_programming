#!/usr/bin/python3
"""
Contains class MyList
"""


class MyList(list):
    """inherits from list
    """
    def print_sorted(self):
        """prints list of ints all sorted in ascending order"""
        print(sorted(self))
