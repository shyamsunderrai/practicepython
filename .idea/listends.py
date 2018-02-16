'''
Take a list and print only and first and last element of the list
a = [5, 10, 15, 20, 25]

- Count elements in the list, probably using len()
- Print index 0 and n
'''


a = [5, 10, 15, 20, 25]

def listends():
    elements = len(a)
    print "First element in the list is: ", (a)[0]
    #Last element
    le = int(elements) - 1
    print "Last element in the list is: " , (a)[le]

listends()