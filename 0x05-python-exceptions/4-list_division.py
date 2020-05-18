1  # !/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    t_error = {
        ZeroDivisionError: 'division by 0',
        TypeError: 'wrong type',
        IndexError: 'out of range'
    }

    for i in range(list_length):
        try:
            n_list.append(my_list_1[i] / my_list_2[i])
        except Exception as error:
            for x in t_error.keys():
                if type(error) == x:
                    print(t_error.get(x))
                    n_list.append(0)

    return (n_list)
