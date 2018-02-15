'''
A palindrome program to accept input from user
and check if the word is palindrome or not

'''

def palindrome():
    mylist=[]
    user_input = raw_input("Enter one word: ")
    wrd = str(user_input)
    rvs = wrd[::-1]

    if (rvs == wrd):
        print user_input + " is a palindrome"
    else:
        print user_input + " is not a palindrome"

palindrome()
