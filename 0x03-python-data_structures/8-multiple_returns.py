#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    if length == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = length, sentence[0]
        return my_tuple
