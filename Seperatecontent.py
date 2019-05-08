# 11. Write a program antihtml.py that takes a URL as argument, downloads the html from web
# and print it after stripping html tags.


from mechanize import Browser
from bs4 import BeautifulSoup
import re,cgi
br = Browser()
br.open('http://indusladies.com')
html = br.response().readlines()
for line in html:
    #print(type(line))
    # print(line)
    lines=line.decode()
    tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
    no_tags = tag_re.sub('', lines)
    ready_for_web = cgi.escape(no_tags)
    print(ready_for_web)
#     cleantext = BeautifulSoup(line)
#     print(cleantext)
# This will not run on online IDE 
# import requests 
# from bs4 import BeautifulSoup 
# import re,cgi
# URL = "http://www.values.com/inspirational-quotes"
# text = requests.get(URL)
# tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

# # Remove well-formed tags, fixing mistakes by legitimate users
# no_tags = tag_re.sub('', text)

# # Clean up anything else by escaping
# ready_for_web = cgi.escape(no_tags)
# print(ready_for_web)
# # soup = BeautifulSoup(r.content, 'html5lib') 
# # print(soup.prettify()) 
