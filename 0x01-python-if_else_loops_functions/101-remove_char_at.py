#!/usr/bin/python3
def remove_char_at(str, n):
    s_list = [c for c in str]
    if n >= 0 and n < len(str):
        del s_list[n]
    return ''.join(s_list)
