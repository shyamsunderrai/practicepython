'''
List comprehension
- Take two lists of different sizes
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- Find the common elements from each list
- Create a new list with common elements, along with elimination of duplicates

'''

import random

def staticlist():
    mylist = []
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    res = [ x for x in a if x in b]
    res1 = list(set(res))
    print res1

def userlist():
    mylist = []
    a1 = random.sample(xrange(20),15)
    a2 = random.sample(xrange(30),25)
    res = [ x for x in a1 if x in a2]
    res1 = list(set(res))
    print res1

staticlist()
userlist()