#!/usr/bin/python3
for i in list(range(97, 123))[::-1]:
    c = chr(i)
    if i % 2:
        c = chr(i - 32)
    print("{:s}".format(c), end='')
