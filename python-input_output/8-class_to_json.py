#!/usr/bin/python3
"""
Contains function that returns dictionary description with
simple data structure(list, dictionary, dictionary, string)
"""


def class_to_json(obj):
    """Class to Json"""
    return obj.__dict__
