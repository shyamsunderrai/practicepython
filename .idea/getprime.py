'''
Accept an input from user and find it its prime number or not

'''

def findifprime():
    user_input = input("Feed me a number between 1 and 100: ")

    if (user_input % 2 != 0):
        print user_input , " Is a prime number"
    else:
        print user_input, " Is an even number"


findifprime()