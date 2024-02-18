#!/usr/bin/python3
"""
Contains method lookup that returns list of object's
"""


def lookup(obj):
    """return list of object's attribute and methods"""
    return dir(obj)
