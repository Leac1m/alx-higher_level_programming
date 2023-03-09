#!/usr/bin/python3

if __name__ == "__main__":
    """_summary_ : prints all arguments past to it"""
    import sys
    
    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    else:
        for i in range(len):
            if i == 0:
                continue
            print("{}: {}".format(i, sys.argv[i]))