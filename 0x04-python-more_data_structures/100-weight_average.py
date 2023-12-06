#!/usr/bin/python3
def weight_average(my_list=[]):
    numerator = 0
    deno = 0
    if my_list:
        for i in range(len(my_list)):
            numerator += my_list[i][0] * my_list[i][1]
            deno += my_list[i][1]
        average = numerator / deno
        return average
    else:
        return 0
