class Fighter:
	def __init__(self, name, nickname, lineage, team, weight_divisions):
		self.name = name
		self.nickname = nickname
		self.lineage = lineage
		self.team = team
		self.weight_divisions = weight_divisions
		return

	def __repr__(self):
		return '{0}, {1}, {2}, {3}, {4}'.format(
			self.name,
			self.nickname,
			self.lienage,
			self.team,
			self.weight_divisions
		)