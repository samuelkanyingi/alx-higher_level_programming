#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = sys.argv[1:]
    res = sum(int(arg) for arg in n)
    print(res)
