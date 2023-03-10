#!/usr/bin/python3

if __name__ == "__main__":
    """_summary_ : prints all arguments past to it"""
    import sys

    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("{} argument:".format(len - 1))
        print("{}: {}".format(len - 1, sys.argv[len - 1]))
    else:
        print("{} arguments:".format(len - 1))
        for i in range(len):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))
