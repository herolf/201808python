# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 08:32:32 2018

@author: Administrator
"""

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


#print str(tags)
movies=[]



for tag in tags:
    limit = 0
    #print limit
    while 1:
        url='https://movie.douban.com/j/search_subjects?type=movie&tag='+tag+'&sort=time&page_limit=1&page_start='+str(limit)
        request = urllib2.Request(url=url)	
        response = urllib2.urlopen(request, timeout=20)
        result = json.loads(response.read())
        result = result['subjects']
       
        if len(result) == 0:
        	break
        limit += 20
        
        #此时的result为列表，赋值给movies后，movies是字典
        for item in result:
            movies.append(item)
            #print item
            #print result
        
        a=movies[0]
        break

        #此时的movies是字典
for x in xrange(0,len(movies)):
    item = movies[x]
    print item['url']
    '''
    request = urllib2.Request(url = item['url'])
    response = urllib2.urlopen(request , timeout = 20)
    result = response.read()
    print result
    
    html = BeautifulSoup(result)
    
    
    title = html.select('h1')[0]
    print title
    ''' 
        
        
       
        
        
        
        
        
        
        
        
        
        

