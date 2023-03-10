#!/usr/bin/python3

if __name__ == "__main__":
    """calcutes according to arguments given.
    Note only +, -, *, / are functional. also to numbers
    at a time."""

    import sys
    import calculator_1 as cal
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        result = cal.add(a, b)
        print(f"{a} + {b} = {result}")
    elif sys.argv[2] == '-':
        result = cal.sub(a, b)
        print(f"{a} - {b} = {result}")
    elif sys.argv[2] == '*':
        result = cal.mul(a, b)
        print(f"{a} * {b} = {result}")
    elif sys.argv[2] == '/':
        result = cal.div(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
