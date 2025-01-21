"""
* Name         : input_functions.py
* Author       : E Wilber
* Created      : 01/19/25
* Module       : 1
* Topic        : 6
* Description  : Gathering Input Functions Assignment
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
print("Find the average of some integers.")
def get_num_of_ints():
    while True:
        try:
            count = int(input("How many integers would you like to enter? "))
            if count < 1:
                print("Error, enter a positive integer.")
            else:
                return count
        except ValueError:
            print("Error, enter a positive integer.")
def get_integers(count, prompt="Enter a number: "):
    integers = []
    for i in range(count):
        while True:
            try:
                if i == count - 1:
                    num = int(input("Enter your last number: "))
                else:
                    num = int(input(prompt))
                integers.append(num)
                break
            except ValueError:
                print("Error, enter a positive integer.")
    return integers
def main():
    count = get_num_of_ints()
    numbers = get_integers(count)
    print("The numbers entered:", numbers)
    average = sum(numbers) / len(numbers)
    print("The average is:", average)
if __name__ == "__main__":
    main()