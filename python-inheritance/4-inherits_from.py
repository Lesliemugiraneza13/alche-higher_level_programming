#!/usr/bin/python3
"""Module that checks if object inherits from specified class"""


def inherits_from(obj, a_class):
    """Returns True if obj is instance of a class that inherited
    from a_class but is not a_class itself"""
    return isinstance(obj, a_class) and type(obj) is not a_class
