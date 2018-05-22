from match import Match

OPPONENT = 1
WINLOSS = 2
METHOD = 3
COMPETITION = 4
WEIGHT = 5
STAGE = 6
YEAR = 7

def parse_method(td):
	if (td.a == None):
		return td.string
	else:
		return td.a.string

def parse_match(tr):
	tds = tr.findAll('td')

	opponent = tds[OPPONENT].span.string
	winloss = tds[WINLOSS].string
	method = parse_method(tds[METHOD])
	competition = tds[COMPETITION].string
	weight = tds[WEIGHT].string
	stage = tds[STAGE].string
	year = tds[YEAR].string

	return Match(opponent, winloss, method, competition, weight, stage, year)