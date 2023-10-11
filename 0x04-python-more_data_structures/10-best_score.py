#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    b_key = None
    b_value = float('-inf')

    for key, value in a_dictionary.items():
        if value > b_value:
            b_value = value
            b_key = key
    return b_key
