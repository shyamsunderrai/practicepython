'''
Writing own binary_search

'''



def find(ordered_list, element_to_find):
    min = 0
    max = len(ordered_list) - 1

    while (min <= max):
        mid = (min + max)/2
        print "Mid is: ", mid , "->", ordered_list[mid]

        if (ordered_list[mid] == element_to_find):
            return True
        elif (ordered_list[mid] < element_to_find):
            min = mid + 1
        else:
            max = mid - 1
    return False


if __name__=="__main__":

    ordered_list = [1,3,5,7,9,11,13,15,17]

    print(find(ordered_list, 5)) # prints False
    print "--->"
    print(find(ordered_list, 7)) # prints False
    print "--->"
    print(find(ordered_list, 20)) # prints False

