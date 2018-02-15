'''
Code to return divisors for a user provided number
# A divisor is like number 13 for 26 because 26/13 has no remainder

- Take user input
- Consider returning divisors between 1 and 100

'''

def returndivisor():
    user_input = input("Enter a number to find its divisors between 2 and 101: ")
    x = range(2,101)
    divisors = []
    for elem in x:
       if ((user_input % elem) == 0):
           divisors.append(elem)
    return divisors

result = returndivisor()
print "Total divisors for your number are: ", result