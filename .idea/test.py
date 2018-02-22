
import datetime

#a = 1517394429
#val = datetime.datetime.fromtimestamp(a)
#print (val.strftime('%Y-%m-%d %H:%M:%S'))

import requests
from bs4 import BeautifulSoup
import tempfile
import StringIO


#with tempfile.SpooledTemporaryFile(max_size=100,
#                                   mode='w+t') as temp:
#    for i in range(3):
#        temp.write('This line is repeated over and over \n')

#    temp.seek(0)
#    for line in temp.read().splitlines():
#        print line
#url = 'http://github.com'
#r = requests.get(url)
#r_html = r.text
#soup = BeautifulSoup(r.text)
#print soup

#myfile = StringIO.StringIO()
#for line in open('/Users/srai/Downloads/application_1517053583409_6503.txt'):
#    myfile.write(line)

#for line in myfile.getvalue().splitlines():
#    print line

#myfile.close()

a = [0, 1, 2, 4]
b = [0, 1, 2, 4]

x = [i for i, j in zip(a, b) if i == j]
print len(x)





