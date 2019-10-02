"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

# import arithmetic.py file containing diff functions

# while loop 
while True:
    # print('hello')

# ask for input form user
    # split the string into a list to get indexes
    user_input = input()
    user_input_tokens = user_input.split(" ")
    # print(user_input_tokens)
# 'q' for quit loop
    if user_input=="q":
        break
    
    if user_input_tokens[0] == '+':
        # print('test')
        print(add(float(user_input_tokens[1]), float(user_input_tokens[2])))

# do if conditionals based on each function from arithmentic.py
    # based on zenith index

