#!/usr/bin/python3
""""define a function that append to a file"""


def append_write(filename="", text=""):
    """function to append and return number of characters"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
