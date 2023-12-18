#!/usr/bin/python3


def magic_calculation(a, b):
    result_num = 0
    for num in range(1, 3):
        try:
            if num > a:
                raise Exception('Too far')
            else:
                result_num += (a ** b) / num
        except Exception:
            result_num = b + a
            break
    return result_num
