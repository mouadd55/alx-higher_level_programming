#!/usr/bin/python3
def multiple_returns(str):
    if 0 == len(str):
        return 0, None
    return len(str), str[0]