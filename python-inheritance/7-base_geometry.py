#!/usr/bin/python3
"""
Module BaseGeometry
====================

This module defines a class `
BaseGeometry` with a method `area()`.

Classes:
--------
- BaseGeometry: A base class
for geometric operations.
"""


class BaseGeometry:
    def integer_validator(self, name, value):
        """
        Validates that `value` is an integer and greater than 0.

        Args:
        name (str): The name of the variable (used in error messages).
        value (any): The value to validate.

        Raises:
        TypeError: If `value` is not an integer.
        ValueError: If `value` is less than or equal to 0.
        """
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        