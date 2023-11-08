#!/usr/bin/python3
"""define read_file function"""


def read_file(filename=""):
    """print utf-8 to stdout"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
