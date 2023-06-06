#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j > i:
            print(f"{i:d}{j:d}", end="")
            if i == 8 and j == 9:
                print('')
            else:
                print(", ", end="")
