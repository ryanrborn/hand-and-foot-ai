# Simulator.py
# the simulator for hand and foot

class Simulator:
	"the simulator for hand and foot"
	players = []
	round = 1
	gameStarted = false
	roundEnd = false
	deck = []
	teamPiles = []

	def addPlayer(self, player):
		if self.gameStarted == false:
			self.players.append(player)

	def startGame(self):
		self.gameStarted = true
		while roundEnd == false:
