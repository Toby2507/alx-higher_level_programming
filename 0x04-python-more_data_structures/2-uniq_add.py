#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    if my_list:
        for t in set(my_list):
            total += t
    return total
