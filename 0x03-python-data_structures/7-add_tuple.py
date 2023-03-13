#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    def fix_tuple(a=()):
        if len(a) == 0:
            return (0, 0)
        if len(a) == 1:
            return (a + (0, ))
        if len(a) == 2:
            return a
        else:
            return a[:2]
    a = fix_tuple(tuple_a)
    b = fix_tuple(tuple_b)
    add = (a[0] + b[0], a[1] + b[1])

    return add
