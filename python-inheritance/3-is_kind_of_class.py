#!/usr/bin/python3

"""
Module is_kind_of_class
Defines a function to check if
"""


def is_kind_of_class(obj, a_class):

    """
    Checks if obj is an instance
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance
    """

    if isinstance(obj, a_class):

        return True
    else:
        return False
