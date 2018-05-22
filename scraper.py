from match import Match
from match_parser import parse_match
from bjj_heroes_souper import get_fighter_url_exts, get_fighter_matches_tr

BASE_URL = 'https://www.bjjheroes.com'
FIGHTER_INDEX_URL = BASE_URL + '/a-z-bjj-fighters-list'

def get_fighter_matches(url):
	fighter_matches = []

	for tr in get_fighter_matches_tr(url):
		fighter_matches.append(parse_match(tr))
	
	return fighter_matches

fighter_url_exts = get_fighter_url_exts(FIGHTER_INDEX_URL)
num_fighters = len(fighter_url_exts)

matches = []

for ext in fighter_url_exts:
	url = BASE_URL + ext
	fighter_matches = get_fighter_matches(url)
	matches.append(fighter_matches)