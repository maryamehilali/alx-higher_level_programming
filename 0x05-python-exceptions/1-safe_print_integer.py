#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = int(value)
        print("{:d}".format(i))
    except Exception:
        return False
    else:
        return True
