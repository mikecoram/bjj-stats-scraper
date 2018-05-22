class Match:
	def __init__(self, opponent, winloss, method, competition, weight, stage, year):
		self.opponent = opponent
		self.winloss = winloss
		self.method = method
		self.competition = competition
		self.weight = weight
		self.stage = stage
		self.year = year

	def __repr__(self):
		return '{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
			self.opponent,
			self.winloss,
			self.method,
			self.competition,
			self.weight,
			self.stage,
			self.year)