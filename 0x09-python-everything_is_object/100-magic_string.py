#!/usr/bin/python3
def magic_string():
    magic_string.magic = getattr(magic_string, 'magic', -1) + 1
    return "Best School, " * magic_string.magic + "Best School"
