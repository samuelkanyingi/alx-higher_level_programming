#!/usr/bin/python3
"""define class base"""

import json
class Base:
    """implement id attribite"""
    __nb_objects = 0
    def __init__(self, id=None):
        """initialize base instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        else:
            raise ValueError("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        class_name = cls.__name__
        filename = f"{class_name}.json"
        try:
            with open(filename, 'r') as file:
                file_content = file.read()
                list_dicts = cls.from_json_string(file_content)
                instances = [cls.create(**item) for item in list_dicts]
                return instances
        except FileNotFoundError:
            return []
