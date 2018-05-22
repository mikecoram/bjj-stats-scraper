from souper import get_soup
from bs4 import BeautifulSoup

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
