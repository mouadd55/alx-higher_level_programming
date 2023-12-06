#!/usr/bin/python3
def delete_at(myList=[], index=0):
    if index < 0 or index >= len(myList):
        return myList
    myList.remove(myList[index])
    return myList
