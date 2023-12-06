#!/usr/bin/python3
def divisible_by_2(myList=[]):
    a = list()
    for i in myList:
        if i % 2 == 0:
            a.append(True)
        else:
            a.append(False)
    return a
