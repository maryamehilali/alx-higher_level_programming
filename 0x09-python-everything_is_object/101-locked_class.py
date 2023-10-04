#!/usr/bin/python3
"""creat a class caled LockedClass"""


class LockedClass:
    """locking the attribute creation except for first_name"""
    __slots__ = ("first_name",)
