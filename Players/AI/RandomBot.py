# RandomBot.py
# a bot that just chooses random options

from Players.AI.AIPlayer import AIPlayer

class RandomBot(AIPlayer):
	"Simple bot that chooses random options"

	def laydown(self, piles, safe, discard, requiredPoints):
		workingHand = []
		if self.inFoot:
			workingHand = self.foot
		else:
			workingHand = self.hand

		options = self.getOptions(workingHand, piles, requiredPoints)