#!/usr/bin/python3
def safe_print_division(a, b):
    quotient = None
    try:
        quotient = a / b
        return quotient
    except Exception:
        return quotient
    finally:
        print("Inside result: {}".format(quotient))
