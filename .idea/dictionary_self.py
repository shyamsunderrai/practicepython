'''
Practicing dictionary function with list

'''

def getcount(file):
    userdict = {}
    with open(file) as myfile:
        line = myfile.readline()

        while line:
            line = line.strip()
            if line in userdict:
                userdict[line] += 1
            else:
                userdict[line] = 1
            line = myfile.readline()

    print userdict


with open('/Users/srai/Downloads/mylist.txt') as myfile:
    line = myfile.readline()

    while line:
        print line
        line = myfile.readline()


#getcount('/Users/srai/Downloads/mylist.txt')