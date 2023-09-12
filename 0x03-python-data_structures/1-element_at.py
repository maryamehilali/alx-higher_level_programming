#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list) - 1
    if idx < 0:
        return None
    elif idx > n:
        return None
    else:
        for i in range(0, n):
            if i == idx:
                return my_list[i]
