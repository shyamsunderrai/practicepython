'''
This python program finds out if input is an ODD or EVEN number


'''

import math

user_input = input("Enter choice of your number: ")

if ((user_input % 2) == 0):
    print "Your input ", user_input , "is an even number"
else:
    print user_input, "is an odd number"
