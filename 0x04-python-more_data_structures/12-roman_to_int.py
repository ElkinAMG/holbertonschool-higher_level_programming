#!/usr/bin/python3


def roman_to_int(roman_string):
    conversion = 0
    if type(roman_string) is str:
        roman_n = {'I': 1, 'V': 5,
                   'X': 10, 'L': 50,
                   'C': 100, 'D': 500,
                   'M': 1000}
        aux = 0
        for char in roman_string:
            for x, y in roman_n.items():
                if char in x:
                    aux += 2 if char in 'I' else 0
                    conversion += y - aux if char != 'I' else y
    return (conversion if conversion < 3999 else 3999)
