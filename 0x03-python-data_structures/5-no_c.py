#!/usr/bin/python3
def no_c(my_string):
    lis_copy = my_string.translate({ord(i): None for i in 'cC'})
    return lis_copy
