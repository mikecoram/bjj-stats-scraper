import urllib2
from bs4 import BeautifulSoup

HEADER = {'User-Agent': 'Mozilla/5.0'}
PARSER_TYPE = 'html.parser'

def get_page(url):
	req = urllib2.Request(url, headers=HEADER)
	return urllib2.urlopen(req)

def get_soup(url):
	return BeautifulSoup(get_page(url), PARSER_TYPE)