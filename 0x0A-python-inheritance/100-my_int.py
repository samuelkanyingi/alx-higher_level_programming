#!/usr/bin/python3i
"""find method in module"""


class MyInt(int):
    """override equality"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality"""
        return super().__eq__(other)
