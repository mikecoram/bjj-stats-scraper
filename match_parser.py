from match import Match

OPPONENT = 		1
WINLOSS = 		2
METHOD = 		3
COMPETITION = 	4
WEIGHT = 		5
STAGE = 		6
YEAR = 			7

def parse_method(td):
	if (td.a == None):
		return td.string
	else:
		return td.a.string

def parse_match(tr, fighter_name):
	tds = tr.findAll('td')

	try:
		opponent = 		tds[OPPONENT].span.string.encode('utf-8')
		winloss = 		tds[WINLOSS].string.encode('utf-8')
		method = 		parse_method(tds[METHOD]).encode('utf-8')
		competition = 	tds[COMPETITION].string.encode('utf-8')
		weight = 		tds[WEIGHT].string.encode('utf-8')
		stage = 		tds[STAGE].string.encode('utf-8')
		year = 			tds[YEAR].string.encode('utf-8')
	except AttributeError:
		print 'AttributeError'
		return None

	return Match(
		fighter_name, 
		opponent, 
		winloss, 
		method,
		competition, 
		weight, 
		stage, 
		year)