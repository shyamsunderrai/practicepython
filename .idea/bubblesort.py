'''
Bubblesort program

1. Take a list of non-sequential numbers
   a = [ 0, 5, 3, 7, 8, 11, 20, 12 ]

2. Create a new list with sorted/arranged list
   out = [ 0, 3, 5, 7, 8, 11, 12, 20 ]

'''

xy = [50, 2, 34, 6, 4, 3, 1, 5, 2]
#xy.sort()
#xy = list(set(xy))
#print xy

def bubblesort():
    mylist = []
    for x in xy:
        for y in xy:
            if (y < x):
                mylist.append(y)

    print mylist

bubblesort()