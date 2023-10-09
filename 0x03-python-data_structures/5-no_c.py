#!/usr/bin/env python3
def no_c(my_string):
    res = ''
    for letter in my_string:
        if letter.lower() != 'c':
            res = res + letter
    return res
