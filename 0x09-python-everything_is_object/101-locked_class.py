#!/usr/bin/python3
"""define class LockedClass"""


class LockedClass:
    """LockedClass prevents user from dynamically creating new instance attributes"""
    __slots__ = ('first_name',)
