#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for i in dictionary:
        if i == key:
            a_dictionary[i] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
