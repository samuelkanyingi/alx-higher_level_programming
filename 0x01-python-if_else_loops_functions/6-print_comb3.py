#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print(f'{i:02},{j:02}', end= ', ' if i != 8 or j != 9 else '\n')
