#!/usr/bin/python3
def multiple_returns(sentence):
    empty = len(sentence)
    if empty == 0:
        return None
    else:
        first = sentence[0]
    return empty, first
