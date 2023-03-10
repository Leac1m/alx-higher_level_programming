#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    len = len(sys.argv)
    if len == 1:
        print("0")
    else:
        sum = 0
        for i in range(len):
            if i == 0:
                continue
            sum += int(sys.argv[i])
        print(sum)
