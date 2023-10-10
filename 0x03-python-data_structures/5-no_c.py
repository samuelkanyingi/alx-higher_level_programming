def no_c(my_string):
    res = ''
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            res = res + letter
    return res
