import sys
from multiprocessing import Pool

from fighter import Fighter
from match import Match
from bjj_heroes_souper import get_fighter_info, get_fighter_url_exts, get_fighter_matches

sys.setrecursionlimit(5000)

# Empty file and write header
with open('matches.csv', 'w') as f:
	f.write('Fighter; Opponent; Result; Method; Competition; Weight; Stage; Year\n')

def process_fighter(ext):
	url = BASE_URL + ext

	fighter_info = get_fighter_info(url)
	fighters.append(fighter_info)

	fighter_matches = get_fighter_matches(url, fighter_info)
	matches.append(fighter_matches)
	with open('matches.csv', 'a') as f:
		for m in fighter_matches:
			if m != None:
				f.write(str(m)+'\n')

	print 'Scraped {0} matches for {1}'.format(
		len(fighter_matches),
		fighter_info)

	return fighter_matches
	
BASE_URL = 'https://www.bjjheroes.com'
FIGHTER_INDEX_URL = BASE_URL + '/a-z-bjj-fighters-list'

fighter_url_exts = get_fighter_url_exts(FIGHTER_INDEX_URL)
num_fighters = len(fighter_url_exts)

print 'Scraping {0} fighters...'.format(num_fighters)

fighters = []
matches = []

pool = Pool(processes=100)	
pool.map(process_fighter, fighter_url_exts)

num_matches = len(matches)

print 'Scraped {0} matches from {1} fighters in {2} seconds.'.format(
	num_matches, 
	num_fighters, 
	0)