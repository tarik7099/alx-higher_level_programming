#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.keys())

    for key in new_list:
        print(f"{key}: {a_dictionary[key]}")
    

    

#print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
