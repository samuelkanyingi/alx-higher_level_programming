#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []
    res = []
    for x in my_list:
        if x % 2 == 0:
            res.append(True)
        else:
            res.append(False)
    return res
