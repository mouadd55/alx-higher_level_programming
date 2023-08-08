#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])
print(f"Last digit of {number} is {str(number)[-1]}", end = " ")
if digit > 5:
    print("and is greater than 5")
elif digit < 6 and digit != 0:
    print("and is less than 6 and not 0")
else:
    print("and is 0")