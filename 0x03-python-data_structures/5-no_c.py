#!/usr/bin/python3
def no_c(my_string):
    trans_table = str.maketrans('', '', 'cC')
    new_string = my_string.translate(trans_table)
    return new_string
