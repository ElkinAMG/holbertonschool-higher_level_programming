#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv[1:])

    if argc == 3:
        number_one, number_two = int(argv[1]), int(argv[3])
        operators = ['+', 'add(number_one, number_two)',
                     '-', 'sub(number_one, number_two)',
                     'x', 'mul(number_one, number_two)',
                     '/', 'div(number_one, number_two)']

        for index, tripper in enumerate(operators):
            if argv[2] == operators[index]:
                print("{:d} {:s} {:d} = {:d}".format(
                    number_one,
                    operators[index],
                    number_two,
                    eval(operators[index + 1])))
                break
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
