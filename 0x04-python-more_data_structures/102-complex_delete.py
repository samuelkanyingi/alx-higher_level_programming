#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k_del = [k for k, val in a_dictionary.items() if val == value]
    for k in k_del:
        del a_dictionary[k]
    return a_dictionary
