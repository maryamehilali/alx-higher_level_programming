#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = int(value)
    except Exception:
        return False
    else:
        print("{:d}".format(i))
        return True
