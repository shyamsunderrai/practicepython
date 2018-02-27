'''
Parsing list of files

'''

#counter_dict = {}
#with open('/Users/srai/Downloads/Test.txt') as f:
#    line = f.readline()

#    while line:
#        line = line.strip()
#        if line in counter_dict:
#            counter_dict[line] += 1
#        else:
#            counter_dict[line] = 1
#        line = f.readline()

#print(counter_dict)


def dict():
    user_dictionary = {}
    with open('/Users/srai/Downloads/Test.txt') as f:
        line = f.readline()

        while line:
            line = line.strip()
            if line in user_dictionary:
                user_dictionary[line] += 1
            else:
                user_dictionary[line] = 1
            line = f.readline()

    print user_dictionary



def enhancedcount():
    counter_dict = {}
    with open('/Users/srai/Downloads/Training.txt') as f:
        line = f.readline()
        while line:
            line = line[3:-26]
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()

    print counter_dict


#dict()
enhancedcount()




