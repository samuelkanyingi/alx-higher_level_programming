#!/usr/bin/python3
"""module to find class"""


class MyList(list):
    """list inheriting from builtin list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
