#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as exp:
        print("Exception:", exp, file=sys.stderr)
        return None
    return fct(*args)
