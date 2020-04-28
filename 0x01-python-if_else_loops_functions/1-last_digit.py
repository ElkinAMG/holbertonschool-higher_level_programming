#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1

if number < 0:
    sign = -1
    value = number % (10 * sign)

if value > 5:
    print("Last digit of {:d} is {:d}\
 and is greater than 5".format(number, value))
elif value == 0:
    print("Last digit of {:d} is {:d}\
 and is 0".format(number, value))
else:
    print("Last digit of {:d} is {:d}\
 and is less than 6 and not 0".format(number, value))
