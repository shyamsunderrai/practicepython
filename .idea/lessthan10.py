'''
Next exercise from practicepython to process this array and make a list/array of numbers that are smaller
than 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

creating an empty list  - x = []
appending value to list - x.append = <value>

iterating through values, can use [ for each in x ]

'''

plist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
sol = []


def listparse ():
    for val in plist:
       if (val < 5):
         sol.append(val)
    return sol

def userparse ():
    userv = input("Enter number: ")
    usol = []
    for val in plist:
        if (val < userv):
            usol.append(val)
    return usol
    print "Your specified value:  ", userv


mylist = listparse()
print "Output of list is ", mylist

userlist = userparse()
print "List < user value", userlist
