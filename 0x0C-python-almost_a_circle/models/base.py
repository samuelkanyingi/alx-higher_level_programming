#!/usr/bin/python3
"""module to find the class"""
import json
import turtle


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor to be called"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns the JSON string representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """method that returns the list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method that returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy_inst = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_inst = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**data) for data in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def draw(list_rectangles, list_squares):
        """function to draw rectangle and square"""
        for _ in range(2):
            turtle.forward(100)
            turtle.forward(90)
            turtle.forward(40)
            turtle.left(90)

        turtle.penup()
        turtle.goto(30, 10)
        turtle.forward(100)
        turtle.pendown()

        for _ in range(2):
            turtle.forward(90)
            turtle.left(90)
            turtle.left(110)
            turtle.left(90)

        turtle.penup()
        turtle.forward(50)
        turtle.goto(110, 90)
        turtle.forward(120)
        turtle.pendown()

        for _ in range(2):
            turtle.forward(20)
            turtle.left(90)
            turtle.forward(25)
            turtle.left(90)
        turtle.penup()
        turtle.forward(100)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(35)
            turtle.left(90)

        turtle.penup()
        turtle.forward(100)
        turtle.goto(70, 50)
        turtle.pendown()

        for _ in range(4):
            turtle.foward(15)
            turtle.left(90)

        turtle.penup()
        turtle.forward(100)
        turtle.goto(30, 70)
        turtle.forward(-100)
        turtle.pendown()
        for _ in range(4):
            turtle.forward(80)
            turtle.left(90)

        turtle.done()
