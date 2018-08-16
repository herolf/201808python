#coding:utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
import urllib
import json
from bs4 import BeautifulSoup



tags=[]
url='https://movie.douban.com/j/search_tags?type=movie'

request = urllib2.Request(url=url)

response = urllib2.urlopen(request, timeout=20)
result = json.loads(response.read())

tags=result['tags']



movies=[]



for tag in tags:

	




	limit = 0

	print limit

	while 1:
		
		url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&sort=time&page_limit=20&page_start='+str(limit)
        
        




        break
		

		#request = urllib2.Request(url=url)
		#print url
		#response = urllib2.urlopen(request, timeout=20)
		#response = urllib2.urlopen(request, timeout=20)
		#response = urllib2.urlopen(request, timeout=20)
        
        #result = response.read()

        

        #result = result['subjects']
        


        
'''       

        request = urllib2.Request(url=url)
		
        response = urllib2.urlopen(request, timeout=20)
        result = response.read()

        

        result = result['subjects']
        
        

        if len(result) == 0:
        	break


        limit += 20

        #print limit

        for item in result:
        	movies.append(item)

        
'''