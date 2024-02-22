#!/usr/bin/python3
"""Module for class Base"""
import json
import os.path


class Base:
    """Parent class in the project"""

    # Number objects created
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Base class"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionary into json string"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of object in a json file"""
        dicts = []
        if list_objs:
            for ins in list_objs:
                dicts.append(cls.to_dictionary(ins))

        json_string = Base.to_json_string(dicts)
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list Pyhton objects from json_string"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Create instances from json file"""
        direc = cls.__name__ + '.json'
        obj = []

        try:
            with open(direc) as f:
                contents = f.read()
        except:
            return obj

        json_data = Base.from_json_string(contents)

        for objects in json_data:
            obj.append(cls.create(**objects))

        return obj
