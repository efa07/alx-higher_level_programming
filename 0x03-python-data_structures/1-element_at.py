#!/usr/bin/python3
def element_at(my_list, idx):
    lis_len = len(my_list)
    if idx < 0 or idx >= lis_len:
        return 'None'
    else:
        return (my_list(idx))
