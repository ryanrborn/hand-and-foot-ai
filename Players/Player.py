# Player.py
# the baseClass player

from Game.Hand import Hand

class Player:
	"the baseClass player"

	def __init__(self, name, hand, foot):
		self.name = name
		self.hand = Hand(hand);
		self.foot = Hand(foot);
		self.inFoot = False

	def draw(self, draw):
		for d in draw:
			if self.inFoot:
				self.foot.addCard(d)
			else:
				self.hand.addCard(d)

	def laydown(self, piles, safe, discard):
		return [];

	def discard(self):
		if self.inFoot:
			return self.foot.pop()
		else:
			return self.hand.pop()

	def isItSafe(self):
		return true