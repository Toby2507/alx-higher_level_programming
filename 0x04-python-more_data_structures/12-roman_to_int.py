#!/usr/bin/python3
def roman_to_int(r_string):
    if r_string is None or not isinstance(r_string, str):
        return 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_numeral = 0
    for i, c in enumerate(r_string):
        c = c.upper()
        if i < len(r_string) - 1 and romans[c] < romans[r_string[i + 1]]:
            roman_numeral -= romans[c]
        else:
            roman_numeral += romans[c]
    return roman_numeral
