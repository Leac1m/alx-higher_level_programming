#!/usr/bin/python3

def no_c(my_string):
    string = ""
    for i in my_string:
        if i in "Cc":
            continue
        string += i
    return (string)
