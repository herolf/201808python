#coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import json
from bs4 import BeautifulSoup



tags=[]
url='http://blog.csdn.net/howeblue/article/details/47426265'
request = urllib2.Request(url=url)
response = urllib2.urlopen(request, timeout=1000)

page = response.read()
print page 
#print result



