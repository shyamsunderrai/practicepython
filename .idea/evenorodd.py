'''
This python program finds out if input is an ODD or EVEN number


'''

import math

def evenorodd():
   user_input = input("Enter choice of your number: ")
   if ((user_input % 2) == 0)  and ((user_input % 4) == 0):
      print "Your input ", user_input , "is an even number divisible by 4"
   elif ((user_input % 2) == 0):
      print "Your input ", user_input, "is an even number"
   else:
    print user_input, "is an odd number"


def checkremainder():
    num = input("Enter first number: ")
    check = input ("Enter second number: ")

    if ((num % check) == 0):
        print num, ": is divisible by ", check
    else:
        print num, ":aint divisble by ", check



evenorodd()
print "Moving to next exercise"
checkremainder()