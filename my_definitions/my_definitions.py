"""
Project: python_packages.py
Author: E Wilber
Last date modified: {12-11-23}

A friendly greeting, the author of the code, a dictionary, and a set. use_my_definitions.py prints this info
"""

def greeting():
    print("Hello there!")

def message():
    print("This code is an example of using Python modules written by E Wilber")

def print_dict(input_dict):
    for key, value in input_dict.items():
        print(f"{key}: {value}")

def print_set(input_set):
    for item in input_set:
        print(item)