import urllib2
from match import Match
from match_parser import parse_match
from bjj_heroes_souper import get_fighter_url_exts, get_player_matches_tr

BASE_URL = 'https://www.bjjheroes.com'
FIGHTER_INDEX_URL = BASE_URL + '/a-z-bjj-fighters-list'

def get_player_matches(url):
	matches = []

	for tr in get_player_matches_tr(url):
		matches.append(parse_match(tr))
	
	return matches

fighter_url_exts = get_fighter_url_exts(FIGHTER_INDEX_URL)

for ext in fighter_url_exts:
	url = BASE_URL + ext
	matches = get_player_matches(url)
	print matches