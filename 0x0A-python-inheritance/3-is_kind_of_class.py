#!/usr/bin/python3
"""define Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """object is an instance or an instance of a class inherited
    Args:
        obj:object
        a_class: class to compare with
    Returns: True if an object is an instance
         or an instance of a class inherited
    """
    return isinstance(obj, a_class)
