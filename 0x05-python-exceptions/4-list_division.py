#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []

    for j in  range(list_length):
        try:
            if  j >= len(my_list_1) or j >= len(my_list_2):
                raise IndexError("out of range")
            num1 = my_list_1[j]
            num2 = my_list_2[j]

            if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
                raise TypeError("wrong type")
            if num2 == 0:
                raise ZeroDivisionError("division by 0")
            res.append(num1/num2)
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
        except TypeError:
            res.append(0)
            print("wrong type")
        except IndexError:
            res.append(0)
            print("out of range")
        finally:
            pass
    return res
