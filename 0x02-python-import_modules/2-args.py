#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    if len(args) > 1:
        print(f"{len(args)} arguments:")
        for i in enumerate(args, 1):
            print(f"{i[0]}: {i[1]}")
    elif len(args) == 1:
        print(f"1 argument:\n1: {args[0]}")
    else:
        print("0 arguments.")
