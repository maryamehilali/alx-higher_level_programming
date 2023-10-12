#!/usr/bin/python3
"""module :creates a function that returns __dict__ of an object”"""


def class_to_json(obj):
    """
    function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    return vars(obj)
