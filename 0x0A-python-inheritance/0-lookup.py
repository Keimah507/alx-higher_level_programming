#!/usr/bin/python3
"""
contains the function lookup
"""


def lookup(obj):
    """function which returns class attributes and methods

    Args:
        obj (obj): the object
    """
    return dir(obj)
