#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        if a < b:
            return a + b
        else:
            c = a - b
            for i in range(4, 6):
                c = c + i

            return c
