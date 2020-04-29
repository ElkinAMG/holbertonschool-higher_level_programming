#!/usr/bin/python3


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            prompt = "FizzBuzz"
        elif number % 3 == 0:
            prompt = "Fizz"
        elif number % 5 == 0:
            prompt = "Buzz"
        else:
            prompt = str(number)

        print(prompt, end=" ")
