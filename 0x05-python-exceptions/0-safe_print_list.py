def safe_print_list(my_list=[], x=0):
    cnt = 0
    try:
        for i in my_list:
            if cnt < x:
                print(i, end='')
                cnt += 1
            else:
                break
        print()
    except IndexError:
        pass
    return cnt
