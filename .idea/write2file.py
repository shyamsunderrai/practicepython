'''
Write output of decoded website to a file
'''

import requests
from bs4 import BeautifulSoup

def writecontent(base_url,location):
    appender = ('http://' + base_url)
    r = requests.get(appender)
    soup = BeautifulSoup(r.text, "html.parser")
    with open(location, 'w') as myfile:
        for story_heading in soup.find_all(class_="story-heading"):
            if story_heading.a:
                print "-------->"
                myfile.write("-------->")
                print(story_heading.a.text.replace("\n", " ").strip())
                myfile.write(story_heading.a.text.replace("\n", " ").strip().encode("utf-8"))
            else:
                print "++++++++>"
                myfile.write("++++++++>")
                print(story_heading.contents[0].strip())
                myfile.write(story_heading.contents[0].strip().encode("utf-8"))

    myfile.close()


if __name__=="__main__":

    iurl = raw_input("Enter the url in this format \" http://xxx.xxxx.xxx \": ")
    iloc = raw_input("Enter the absolute path and name of file to write content \"/Users/srai/Downloads/xxxx.txt\": ")

    writecontent(iurl,iloc)
