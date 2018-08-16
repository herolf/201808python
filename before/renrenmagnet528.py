# coding: utf-8
 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import re

f = open('4.txt')

for line in f:
	ma = re.search(r'(")(magnet:.+?)(">)',line)
	if ma is not None:
		print ma.group(2)

f.close()