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
import io
import StringIO


def parseyarnapp1():
    plist = []
    sew = []
    for line in yarnappfile.getvalue().splitlines():
        if "Starting to run new task attempt" in line or "Completed running task attempt" in line:
            mylist.append(line.split("attempt:")[1].rstrip('\n').lstrip(' '))
            result = list(set(mylist))

    yarnappfile.seek(0)
    for item in mylist:
        for line in yarnappfile.getvalue().splitlines():
            if item in line and "history.HistoryEventHandler" in line and "Event:TASK_ATTEMPT_" in line and "status=" in line:
                plist.append(line)

    for item in plist:
        attempt= item.split(": ")[2].split(", ")[1].split("taskAttemptId=")[1]
        vertex= item.split(": ")[2].split(", ")[0].split("vertexName=")[1]
        timetaken = int(item.split(": ")[2].split(", ")[6].split("timeTaken=")[1])
        r1 = str(vertex),str(attempt),int(timetaken)
        sew.append(r1)
        result = list(set(sew))
    return result


def longrunning():
    result = []
    output = parseyarnapp1()
    output.sort(key=lambda x:x[2],reverse=True)
    print "You can list all tasks with time taken to complete Or you can specify a number of lines you wish to see"
    uinput = int(input("Enter the number of tasks you wish to list: "))
    for val in range(0,uinput):
        result.append(output[val])
        print output[val]
    return result


def getcounters():
    #Attempts to sort from buffer
    a2s = []
    print "Retrieving counters details for retrieved attempts"
    attempts = longrunning()
    for attempt in attempts:
        a2s.append(attempt[1])

    for line in yarnappfile.getvalue().splitlines():
        for item in a2s:
            if item in line and 'org.apache.tez.common.counters.TaskCounter' in line:
                print "- - - - - Counters for ", item, " - - - - -"
                print line

# Running main code here

user_input= raw_input("Enter name of the application Log: ")
mylist=[]
yarnappfile = StringIO.StringIO()
for line in open(user_input):
    yarnappfile.write(line)

getcounters()
yarnappfile.close()


