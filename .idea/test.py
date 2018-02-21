
import datetime

#a = 1517394429
#val = datetime.datetime.fromtimestamp(a)
#print (val.strftime('%Y-%m-%d %H:%M:%S'))

import requests
from bs4 import BeautifulSoup
import tempfile

with tempfile.SpooledTemporaryFile(max_size=100,
                                   mode='w+t') as temp:
    for i in range(3):
        temp.write('This line is repeated over and over.\n')

    temp.seek(0)
    print temp.read()
#url = 'http://github.com'
#r = requests.get(url)
#r_html = r.text
#soup = BeautifulSoup(r.text)
#print soup


