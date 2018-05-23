from souper import get_soup
from bs4 import BeautifulSoup
from match import Match
from match_parser import parse_match

def get_fighter_url_exts(index_url):
	soup = get_soup(index_url)
	table_rows = soup.tbody.findAll('tr')

	fighter_url_exts = []
	for tr in table_rows:
		fighter_url_exts.append(tr.a['href'])
	return fighter_url_exts

def get_fighter_matches_tr(url):
	soup = get_soup(url)
	
	if (soup.tbody != None):
		return soup.tbody.findAll('tr')
	else:
		return []

def get_fighter_matches(url):
	fighter_matches = []

	for tr in get_fighter_matches_tr(url):
		fighter_matches.append(parse_match(tr))
	
	return fighter_matches

def get_fighter_info(url):
	soup = get_soup(url)
	name = soup.h1.string.encode('utf-8')
	return name
