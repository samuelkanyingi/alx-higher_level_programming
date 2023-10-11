#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return None
    t_sum = 0
    t_weight = 0

    for i, j in my_list:
        t_sum += i * j
        t_weight = t_weight + j

    if t_weight == 0:
        return 0
    else:
        return t_sum / t_weight
