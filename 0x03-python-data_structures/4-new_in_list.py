#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lis_len = len(my_list)
    new_lis = my_list.copy()
    if idx < 0 or idx > lis_len - 1:
        return new_lis
    else:
        new_lis[idx] = element
        return new_lis  
