#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv[1:])

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, b = int(argv[1]), int(argv[3])
    sign = argv[2]
    operators = ['+', 'add(a, b)',
                 '-', 'sub(a, b)',
                 '*', 'mul(a, b)',
                 '/', 'div(a, b)']

    for index, tripper in enumerate(operators):
        if sign == operators[index]:
            print("{:d} {:s} {:d} = {:d}".format(
                a,
                sign,
                b,
                eval(operators[index + 1])))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
