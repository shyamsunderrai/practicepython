'''
Generate random password
- Password should contain letters in lower case
- Password should contain letters in Upper case
- Password should contain symbols
- Password should contain numbers
- Should be between 8 - 15 characters long

Use inbuilt random function to generate password

'''

import random
import string

def genpass():
    mylist = []
    slist = ['!','@','#','$','%','^','&','*','(',')','{','{']

    for e in slist:
        st = random.choice(string.letters)
        ine = random.randrange(0,101,4)
        rl = random.choice(slist)
        choices = (st+str(ine)+e+rl+st+str(ine)+e+rl)
        mylist.append(choices)

    population = mylist[0:4]
    print "Your password is:", random.choice(population)

genpass()



