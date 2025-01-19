"""
* Name         : twice_function_decorator.py
* Author       : E Wilber
* Created      : 01/19/25
* Module       : 1
* Topic        : 7
* Description  : Do it Twice Function Decorator Assignment
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
#Defining the decorator
def run_twice(func):
    def wrapper(*args, **kwargs):
        print("This output is from running a function twice:")
        func(*args, **kwargs)  #1st call
        func(*args, **kwargs)  #2nd call
    return wrapper
#putting the decorator on th function
@run_twice
def greet(name):
    print(f"Hi {name}!")
# Calling the decorated function
greet("Professor Buys")
