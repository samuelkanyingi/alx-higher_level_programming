#!/usr/bin/python3
"""module to get method"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    with open(filename, 'r') as file:
        line_text = file.readlines()

    with open(filename, 'w') as file:
        for l_txt in line_text:
            file.write(l_txt)
            if search_string in l_txt:
                file.write(new_string + '\n')
