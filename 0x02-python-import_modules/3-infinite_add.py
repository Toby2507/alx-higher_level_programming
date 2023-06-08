#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = argv[1:]
    res = 0
    for arg in args:
        res += int(arg)
    print(res)
