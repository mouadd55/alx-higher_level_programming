#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        flag = 0
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            flag = 32
        print("{}".format(chr(ord(str[i]) - flag)), end='')
    print()
