# hand.py
# this is what controls a hand

class Hand:
	"a hand of cards"

	def __init__(self, cards):
		self.piles = {}
		self.numCards = 0
		"array of cards is passed, put them into the dictionary"
		for card in cards:
			self.addCard(card)

	def addCard(self, card):
		# print card.toString()
		if card.getCard() not in self.piles:
			self.piles[card.getCard()] = []

		self.piles[card.getCard()].append(card)
		self.numCards += 1

	def getTypes(self):
		return self.piles.keys();

	def getCardCount(self, card):
		if card not in self.piles:
			return 0
		else:
			return len(self.piles[card])

	def toString(self):
		string = ""
		for k,v in self.piles.iteritems():
			string += "'"+k+"':%d\n" % len(v)
		return string