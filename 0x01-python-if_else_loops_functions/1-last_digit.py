#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_di = int(str(number)[-1])
if last_di == 0:
    print("Last digit of {} is 0 and is 0".format(number))
elif last_di > 5:
    print("Last digit of {} is {} and is greater than 5 and not 0".format(number,last_di))
elif last_di < 6 and not 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_di))
