#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list
    lis_len = len(my_list)
    if idx < 0 or idx >= lis_len:
        return new_list
    else:
        new_list[idx] = element
        return new_list
    
