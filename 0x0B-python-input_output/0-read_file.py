#!/usr/bin/python3
"""module to find method"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
