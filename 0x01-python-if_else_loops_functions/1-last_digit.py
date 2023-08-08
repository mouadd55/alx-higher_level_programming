#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = int(str(number)[-1])
if number < 0:
    digit *= -1
print("Last digit of {} is {}".format(number, digit), end=" ")
if digit == 0:
    print("and is 0")
elif digit > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
