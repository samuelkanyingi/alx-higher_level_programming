#!/usr/bin/python3
""""define a append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file
    Args:
        filename: name of file
        search_string: string to loook for in each line
        new_string: appended lin eof text
    """
    with open(filename, 'r') as file:
        line_s = file.readlines()

    with open(filename, 'w') as file:
        for lin in line_s:
            file.write(lin)
            if search_string in lin:
                file.write(new_string)
