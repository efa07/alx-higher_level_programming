#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis_len = len(my_list)
    my_lis_copy = my_list.copy()
    if idx < 0 or idx >= lis_len:
        return my_lis_copy
    else:
        my_lis_copy[idx] = element
        return my_lis_copy   
