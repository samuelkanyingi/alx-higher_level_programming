#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    try:
        for i in my_list:
            if cnt >= x:
                break
            try:
                print("{:d}".format(i), end='')
                cnt += 1
            except (ValueError, TypeError):
                pass
        print()
    except IndexError:
        pass
    return cnt
