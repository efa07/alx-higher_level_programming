#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = my_list
        new_list[idx] = new_element
        return new_list

