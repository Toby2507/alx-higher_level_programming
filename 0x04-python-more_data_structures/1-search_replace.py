#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = my_list[:]
    return [replace if n is search else n for n in n_list]
