#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i and i != 8:
            print("{}{}".format(i, j), end=", ")
        elif i == 8 and j == 9:
            print("{}{}".format(i, j))
            break
