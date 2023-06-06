#!/usr/bin/python3
def uppercase(str):
    for c in str:
        c_upper = c
        if ord(c) in range(97, 123):
            c_upper = chr(ord(c) - 32)
        print(c_upper, end='')
    print()
