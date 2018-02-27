'''
Creating a binary search, working with a sorted list
a = [1,3,5,7,9,11,13,15]

'''



#for item in a:
#    if (item == 9):
#        print "9 is in the list"

def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


#if __name__=="__main__"

l = [2, 4, 6, 8, 10]
#    print (find(l, 5))

#Assuming l is the ordered list
def binfind(ordered_list, element_to_find):
    start_index = 1 # 1 stores value 2
    end_index = len(ordered_list) - 1 # 5 (end_index) stores value 5


    while True:
        middle_index = (end_index - start_index)/2 # 5 - 1 /2 = position 2 and value 6

        print "Step 1, end_index is:", end_index
        print "Step 1, start_index is:", start_index
        print "Step 1, middle_index is:", middle_index

        if middle_index < start_index or middle_index > end_index or middle_index < 0:
            return False

        middle_element = ordered_list[middle_index] # Position 2 and value 6
        print "Step 2, middle_element is:", middle_element

        if middle_element == element_to_find:
            return True
        elif middle_element < element_to_find:
            end_index = middle_index
        else:
            start_index = middle_index


print binfind(l, 8)


