'''
Write output of decoded website to a file
'''

import requests
from bs4 import BeautifulSoup

def writecontent(base_url,location):
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