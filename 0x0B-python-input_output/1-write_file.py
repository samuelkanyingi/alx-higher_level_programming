#!/usr/bin/python3
"""define a funtion to write to a file"""


def write_file(filename="", text=""):
    """function that writes to text file and return number of characters"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
