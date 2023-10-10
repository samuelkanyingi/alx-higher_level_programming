#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x, num in enumerate(i):
            print('{:2d}'.format(num), end=' ' if x < len(i) - 1 else "\n")
