#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number % -10
    else:
        number = number % 10
    if number < 0:
        number *= -1
    print("{:d}".format(number), end="")
    return (number)
