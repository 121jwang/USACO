class Team:
	teamNum = 0;
	def __init__(self, number):
		teamNum = number;
	def getConnect(self, otherTeam):
		return teamNum ^ otherTeam
	
