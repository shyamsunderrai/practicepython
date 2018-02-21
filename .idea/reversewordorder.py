'''
Reverse word order

For
"My name is Shyam"
print
"Shyam is name My"
'''

def reverse(input):
    mylist = user_input.split(' ')
    le = len(mylist)
    print mylist[le::-1]

user_input=raw_input("Introduce yourselves (My name is <Your name>: ")
reverse(user_input)
