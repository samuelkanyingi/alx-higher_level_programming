#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ab_num = abs(number)
last_num = ab_num % 10
if last_num > 5:
    msg = f'and is greater than 5'
elif last_num == 0:
    msg = f'and is 0'
else:
    msg = f'and is less than 6 and not 0'
print(f'Last digit of {number} is {last_num}, {msg}')
