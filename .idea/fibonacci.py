'''
Generating Fibonacci sequence upon users request
- Take input from user on how many Fibonacci numbers to generate
- Generate that many number of Fibonacci numbers in the output

if User input is: 10
1. Create a list with two values 1,1 as they are always there in the fibonacci sequence
2. Take two variabels for last and second last values in the list index
   x= len(list)-1
   y= len(list)-2
   Thus, if a list has two values [1,1], then, x =1 and y = 1
3. Take an integer and assign the sum of x + y
4. Append the list with the new sum
5. Keep track of count by incrementing it with len(list) i.e., count = len(list) so that loop can complete
6. When the loop moves to next iteration, value of x will be 2 and y will be 1,and so on

'''

def fibonacci ():
    user_input= int(input("Enter number of Fibonacci  sequences to generate: "))
    count = 0
    fint = 0
    flist = [1,1]

    while (count != user_input):
        le = len(flist)-1
        sle = len(flist)-2
        fint =  flist[sle] + flist[le]
        flist.append(fint)
        count = len(flist)

    print flist

fibonacci()