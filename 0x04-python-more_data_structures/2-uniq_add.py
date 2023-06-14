#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        total = 0;
        for t in set(my_list):
            total += t
        return total
