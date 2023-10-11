#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []
        for j in row:
            s = j ** 2
            new_row.append(s)
        new_matrix.append(new_row)
    return new_matrix
