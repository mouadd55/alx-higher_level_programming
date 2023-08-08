#!/usr/bin/python3
for i in range(10):
    j = i + 1
    while (j < 10):
        print("{}{}".format(i, j), end="")
        if (i < 8):
            print(", ", end="")
        j = j + 1
print()
