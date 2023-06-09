#!/usr/bin/python3
def no_c(my_string):
    str_n = [char for char in my_string if char not in "cC"]
    return ''.join(str_n)
