

'''
Program will take two inputs:
- Name
- Integer (age)
-- Used raw_input for accepting values for either name and age.
-- Used int(raw_input()) for converting input to integer format

Return the YEAR in which the user will turn 100

'''

import datetime

now = datetime.datetime.now()
name = raw_input("Enter your name: ")
age = int(raw_input("Enter you age in years: "))

# x + age = 100
# x = ?
# 100 - age = x
xage = 100 - age
xyear = now.year
finalyear = xage + xyear

print (name + "You will be 100 years old in the year: ", finalyear)