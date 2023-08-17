#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        biggest = -1
        key_name = None
        for key, value in a_dictionary.items():
            if value > biggest:
                biggest = value
                key_name = key
        return key_name
    else:
        return (None)
