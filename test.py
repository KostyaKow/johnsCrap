#!/usr/bin/python3

import requests
from html.parser import HTMLParser
#https://docs.python.org/3/library/html.parser.html


class ParseGoogle(HTMLParser):
   def __init__(self):
      self.prt = True
      super(ParseGoogle, self).__init__()

   def handle_starttag(self, tag, attrs):
      #print(tag)
      #print(attrs)
      if tag == 'h3':
         self.prt = True
      pass
   def handle_endtag(self, tag):
      #print(tag)
      if tag == 'h3':
         self.prt = False
      pass
   def handle_data(self, data):
      if self.prt:
         print(data)

def search(question):
   s = "https://google.com/search?q=%s" % question
   r = requests.get(s)
   #print(r)
   return r.text

parser = ParseGoogle()
parser.feed(search('sdgsd'))
#print(search('sdgsd'))


