class Match:
	def __init__(self, fighter, opponent, winloss, method, competition, weight, stage, year):
		self.fighter = fighter
		self.opponent = opponent
		self.winloss = winloss
		self.method = method
		self.competition = competition
		self.weight = weight
		self.stage = stage
		self.year = year

	def tostring(self):
		return '{0}; {1}; {2}; {3}; {4}; {5}; {6}; {7}'.format(
			self.fighter,
			self.opponent,
			self.winloss,
			self.method,
			self.competition,
			self.weight,
			self.stage,
			self.year)

	def __str__(self):
		return self.tostring()

	def __repr__(self):
		return self.tostring()
