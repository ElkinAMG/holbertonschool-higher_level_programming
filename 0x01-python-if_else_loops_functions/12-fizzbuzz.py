#!/bin/usr/python3


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0 or number % 5 == 0:
            if number % 3 == 0:
                print("Fizz", end=" ")
            else:
                print("Buzz", end=" ")
        else:
            print(number, end=" ")
