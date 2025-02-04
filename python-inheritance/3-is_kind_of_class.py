#!/usr/bin/python3
"""
Module is_kind_of_class
Defines a function to check if an object is an instance of a class or its subclass.
"""
def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or an instance of a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    if isinstance(obj,a_class):
        return True
    else:
        return False
