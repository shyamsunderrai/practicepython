
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