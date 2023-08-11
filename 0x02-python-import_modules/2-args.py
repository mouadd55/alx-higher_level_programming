#!/usr/bin/python3
import sys

if __name__ == '__main__':
    length = len(sys.argv)
    if length == 1:
        print("0 arguments.")
    else:
        print(f"{length - 1} arguments:")
        for i, arg in enumerate(sys.argv[1:]):
            print(f"{i + 1}: {arg}")
