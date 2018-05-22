from fighter import Fighter
from match import Match
from bjj_heroes_souper import get_fighter_info, get_fighter_url_exts, get_fighter_matches

BASE_URL = 'https://www.bjjheroes.com'
FIGHTER_INDEX_URL = BASE_URL + '/a-z-bjj-fighters-list'

fighter_url_exts = get_fighter_url_exts(FIGHTER_INDEX_URL)
num_fighters = len(fighter_url_exts)

print 'Scraping {0} fighters...'.format(num_fighters)

fighters = []
matches = []

i = 1

for ext in fighter_url_exts:
	url = BASE_URL + ext

	fighter_info = get_fighter_info(url)
	fighters.append(fighter_info)

	fighter_matches = get_fighter_matches(url)
	matches.append(fighter_matches)

	print '{0}:Scraped {1} matches for {2}'.format(
		i,
		len(fighter_matches),
		fighter_info
	)

	i += 1

num_matches = len(matches)

print 'Scraped {0} matches from {1} fighters in {3} seconds.'.format(
	num_matches, 
	num_fighters, 
	0)