#!/usr/bin/python3
def pow(a, b):
    res = 1
    for x in range(abs(b)):
        res = res * a
    if b < 0:
        return 1 / res
    return res
