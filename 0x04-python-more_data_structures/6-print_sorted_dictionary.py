#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    r = dict(sorted(a_dictionary.items()))
    for key, x in r.items():
        print(key, ':', x)
