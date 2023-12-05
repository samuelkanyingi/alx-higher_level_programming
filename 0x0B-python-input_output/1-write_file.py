#!/usr/bin/python3
"""module to find method"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
