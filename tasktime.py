#!/usr/bin/env python

'''
## Whats happening here !!
1. Enter the filename and then parse it for one of the following phrases:
   'Starting to run new task attempt'
   'Completed running task attempt'

2. Once the attempt ID's are obtained, make a list of unique attempt IDs

3. For each attempt ID, fetch the start/end time by parsing both the strings
   obtained in Step 1

4. Subtract "Completed..." timestamp with "Starting..." timestamp to figure 
   out which task is taking longest

'''

import datetime
import time
import re

user_input= raw_input("Enter name of the application Log: ")
mylist=[]

def parseyarnapp():
   for line in open(user_input):
      if "Starting to run new task attempt" in line or "Completed running task attempt" in line:
          mylist.append(line.split("attempt:")[1].rstrip('\n').lstrip(' '))
          result = list(set(mylist))  
          
   for item in result:
      for line in open(user_input):
         if "Completed running" in line and item in line:
            etime = line.strip("")[11:19]
	 if "Starting to" in line and item in line:
            stime = line.strip("")[11:19]
      
      FMT='%H:%M:%S'
      elapsed = (datetime.datetime.strptime(etime, FMT) - datetime.datetime.strptime(stime, FMT))
      regex = re.compile('[a-z]|[A-Z]')
      if (regex.findall(str(elapsed))):
         print item, ":  0"
      else:
         stripped = str(elapsed).strip(":")[5:7]
         print item, ": ", stripped
      
         
parseyarnapp()   



