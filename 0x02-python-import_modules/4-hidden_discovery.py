#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for tripper in dir(hidden_4):
        if tripper[:2] not in "__":
            print(tripper)
