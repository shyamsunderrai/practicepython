'''
Remove duplicates from list

Work with two different functions to perform
  a. First function to return a new list without duplicate element using sets
  b. Second function to return a new list without duplicates, however, without using sets

mlist = [ 1, 2, 5, 7, 9, 5, 2, 8, 6, 3, 1 ]

'''

mylist = []
mlist = [ 1, 2, 5, 7, 9, 5, 2, 8, 6, 3, 1 ]

def listsets():
    mylist = list(set(mlist))
    print mylist

def listloop():
    mylist = []
    for element in mlist:
        if element not in mylist:
            mylist.append(element)
    print mylist

#listsets()
listloop()

