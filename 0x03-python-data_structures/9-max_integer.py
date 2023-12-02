#!/usr/bin/python3
def max_integer(my_list=[]):
    lis_len = len(my_list)
    if lis_len == 0:
        return "None"
    else:
        max_int = my_list[0]
        for i in range(lis_len):
            if my_list[i] > max_int:
                max_int = my_list[i]
        return max_int
