#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args_len = len(sys.argv)
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    opra = sys.argv[2]
    b = int(sys.argv[3])

    if opra == '+':
        print("{} {} {} = {}".format(a, opra, b, add(a, b)))
    elif opra == '-':
        print("{} {} {} = {}".format(a, opra, b, sub(a, b)))
    elif opra == '*':
        print("{} {} {} = {}".format(a, opra, b, mul(a, b)))
    elif opra == '/':
        print("{} {} {} = {}".format(a, opra, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
