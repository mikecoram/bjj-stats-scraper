import urllib2
from bs4 import BeautifulSoup

HEADER = {'User-Agent': 'Mozilla/5.0'}
PARSER_TYPE = 'html.parser'

def get_page(url):
	req = urllib2.Request(url, headers=HEADER)
	res = None

	try:
		res = urllib2.urlopen(req)
	except urllib2.HTTPError:
		raise Exception('Page exception')

	return res

def get_soup(url):
	try:
		soup = BeautifulSoup(get_page(url), PARSER_TYPE)
	except Exception:
		raise Exception('Soup exception')
	return soup