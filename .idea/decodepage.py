'''
Decode a web page using Beautifulsoup

'''

import requests
from bs4 import BeautifulSoup

url = 'https://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.6.0/bk_release-notes/content/fixed_issues.html'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
print soup.find('div','td')

