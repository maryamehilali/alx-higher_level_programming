#!/usr/bin/python3
"""module for Base class"""
import json
import os


class Base(object):
    """the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON string
        representation json_string"""
        if json_string is None or json_string == "":
            return "[]"
        else:
            return [json.loads(json_string)]

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_dict = []
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, mode="w", encoding="utf-8") as a_file:
            a_file.write(Base.to_json_string(list_dict))

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        file_name = "{}.json".format(cls.__name__)
        list_inst = []
        if not os.path.exists(file_name):
            return list_inst
        else:
            with open(file_name, "r", encoding="utf-8") as a_file:
                list_dictn = cls.from_json_string(a_file.read())
                list_inst = [cls.create(cls, **i) for i in list_dictn] 
                return list_inst
