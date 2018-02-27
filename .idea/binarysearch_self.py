'''
Creating a binary search program from a list of numbers
'''

def find(mlist,e2f):
    min = 0
    max = len(mlist) - 1

    while (min <= max):
        mid = (min + max)/2
        mid_element = mlist[mid]

        if (mid_element == e2f):
            return True
        elif (mlist[mid] < e2f):
            min = mid + 1
        else:
            min = mid - 1

        print "mid_element: ", mid_element
        print "mid is: ", mid
        print "min is: ", min
        print "max is: ", max

    return False




if __name__ == "__main__":

    mylist = [24,6,8,10,12,14]
    print (find(mylist,14))


