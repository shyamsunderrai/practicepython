'''
Contains challenges with extras as well.

Generate a list of common elements from these two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

1. Use for loop to iterate through each element in both arrays
2. Create an empty list
3. Append to list when elements match
4. Find a way to ensure that no duplicates are allowed in the presented list

'''

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
collection = []

def topyfor():
   x = [ c for c in b if c in a]
   y = list(set(x))
   print y

def randompyfor():
   x = random.sample(xrange(15),10)
   y = random.sample(xrange(20),14)
   print "User generated list: -----"
   print list(x)
   print list(y)
   print "- - - - - - - - - - - - - -"
   res = [a for a in x if a in y]
   res1 = list(set(res))
   print res1

topyfor()
randompyfor()






