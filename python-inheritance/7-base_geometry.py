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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        