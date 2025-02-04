#!/usr/bin/python3
"""
Module BaseGeometry
====================

This module defines a class `BaseGeometry` with a method `area()`.

Classes:
--------
- BaseGeometry: A base class for geometric operations.
"""

class BaseGeometry:
    """
    A base class for geometry-related operations.

    Methods:
    --------
    - area(self): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Raises an Exception indicating that the method is not yet implemented.

        Raises:
            Exception: Always raises with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
