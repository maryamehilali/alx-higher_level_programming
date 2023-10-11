#!/usr/bin/python3
"""module :write a object into a file using  JSON string"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        return a_file.write(json.dumps(my_obj))
