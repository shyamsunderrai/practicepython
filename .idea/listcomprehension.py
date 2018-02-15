'''
List comprehension
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Challenge is to make a new list in one line that contains only
even numbers

'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = []

def sortlist():
    for val in a:
        if ((val %2) == 0):
            x.append(val)
    return x

xx = [x for x in a if x % 2 == 0]
print list(xx)


#result = sortlist()
#print result



