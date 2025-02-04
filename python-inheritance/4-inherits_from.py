#!/usr/bin/python3
"""
Module inherits_from
====================

This module defines the function `inherits_from()` that checks whether an object
is an instance of a class that directly or indirectly inherited from another class.

Function:
-----------
- inherits_from(obj, a_class): Returns True if the object is an instance of a class
  that inherits (directly or indirectly) from `a_class`, otherwise returns False.
"""

def inherits_from(obj, a_class):
    """
    Checks if an object `obj` is an instance of a class that inherited from `a_class`.

    Args:
        obj (object): The object to test.
        a_class (type): The class to compare against.

    Returns:
        bool: Returns True if `obj` is an instance of a class that inherits from `a_class`
              (directly or indirectly), otherwise returns False.
    """
    if isinstance(obj, object) and issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
