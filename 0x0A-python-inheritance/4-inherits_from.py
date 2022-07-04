#!/usr/bin/python3
"""
contains function inherits_from
"""


def inherits_from(obj, a_class):
    """returns true if obj inherited from specified class; otherwise false"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
