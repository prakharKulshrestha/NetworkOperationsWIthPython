import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen('https://wiki.python.org/moin/').read()

parsedObj = BeautifulSoup(html, 'html.parser')

aList=parsedObj('a')
for anchor in aList:
	print (anchor.get('href',None))
