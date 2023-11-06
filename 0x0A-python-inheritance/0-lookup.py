#!/usr/bin/python3
"""Define obj attributes func"""


def lookup(obj):
    """Return obj attribute list"""
    attr_methods = dir(obj)
    return (attr_methods)
