#!/usr/bin/python3
def best_score(a_dictionary):
    big = ""
    value1 = 0
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if value > value1:
            value1 = value
            big = key
    return big
