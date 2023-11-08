#!/usr/bin/python3
"""define class student"""


class Student:
    """represemy student first name, lastname and age"""
    def __init__(self, first_name, last_name, age):
        """initialize
        Args:
            first_name:firstname of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }
