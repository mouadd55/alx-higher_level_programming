#!/usr/bin/python3
def max_integer(myList=[]):
    if 0 == len(myList):
        return None
    return sorted(myList)[-1]
