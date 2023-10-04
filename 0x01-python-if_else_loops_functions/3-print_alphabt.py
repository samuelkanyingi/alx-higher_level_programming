#!/usr/bin/python3
for askey in range(ord('a'), ord('z')+1):
    if chr(askey) not in ['q', 'e']:
        print(chr(askey), end='')
