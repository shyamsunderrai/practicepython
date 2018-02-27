'''
Testing out http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html
BeautifulSoup documentation:  http://www.crummy.com/software/BeautifulSoup/bs4/doc/#making-the-soup
Requests documentation: http://docs.python-requests.org/en/latest/user/install/#install

'''

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'

def geturl():
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")

    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            print "-------->"
            print(story_heading.a.text.replace("\n", " ").strip())
        else:
            print "++++++++>"
            print(story_heading.contents[0].strip())


if __name__=="__main__":
    geturl()