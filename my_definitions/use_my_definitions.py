"""
Project: python_packages.py
Author: E Wilber
Last date modified: {12-11-23}

uses my_definitions.py to print a friendly greeting, print the author of the code, prints pairs from a dictionary, and
prints from a set one item per line
"""
import my_definitions

# Call functions from the my_definitions module
my_definitions.greeting()
my_definitions.message()

# Example dictionaries and sets
example_dict = {"a": 1, "b": 2, "c": 3}
example_set = {1, 2, 3}

# Using the functions in my_definitions module
my_definitions.print_dict(example_dict)
my_definitions.print_set(example_set)