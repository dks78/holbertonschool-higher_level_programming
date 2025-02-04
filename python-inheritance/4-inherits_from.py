#!/usr/bin/python3
"""
Module inherits_from
====================

This module defines the func
is an instance of a class th

Function:
-----------
- inherits_from(obj, a_
  that inherits (directly
"""


def inherits_from(obj, a_class):

    """
    Checks if an object `

    Args:.

    Returns:
              (dir
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
