#!/usr/bin/python3
"""module :creates a Student class”"""


class Student(object):
    """create the Student Class"""
    def __init__(self, first_name, last_name, age):
        """instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that retrieves a dictionary representation
        of a Student instance
        """
        if type(attrs) == list and all(type(nm) == str for nm in attrs):
            return dict((key, vars(self)[key]) for key in attrs
                        if key in vars(self))
        else:
            return vars(self)

    def reload_from_json(self, json):
        """
        function that replaces all attributes of the Student instance
        """
        for attr in json:
            if attr in vars(self):
                setattr(self, attr, json[attr])
