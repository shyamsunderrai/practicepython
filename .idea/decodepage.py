'''
Decode a web page using Beautifulsoup

'''

import requests
from bs4 import BeautifulSoup

url = 'http://github.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")
title = str(soup.find('span','articletitle'))
print title

