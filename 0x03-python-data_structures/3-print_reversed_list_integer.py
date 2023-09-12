#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    n = len(my_list)
    for i in range(n, 0, -1):
        print("{:d}".format(i))
