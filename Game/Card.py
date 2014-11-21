# Card.py
# just a simple card

class Card:
	"A Simple Card"

	def __init__(self, suite, card):
		self.suite = suite
		self.card = card
		if card == 'R':
			self.points = 50
		elif card == 'A' or card == '2':
			self.points = 20
		elif card == 'K' or card == 'Q' or card == 'J' or card == '0':
			self.points = 20
		elif card == '3':
			if suite == 'D' or suite == 'H':
				self.points = -300
			else:
				self.points = -100
		else:
			self.points = 5

	def getPoints(self):
		return self.points

	def getSuite(self):
		return self.suite

	def getCard(self):
		return self.card

	def getColor(self):
		if self.suite == 'C' or self.suite == 'S':
			return 'black'
		else:
			return 'red'

	def isWild(self):
		return self.card == '2' or self.card == 'R'

	def toString(self):
		if(self.card == 'R'):
			return "Joker"

		string = ""
		if self.card == 'A':
			string += 'Ace'
		elif self.card == 'J':
			string += 'Jack'
		elif self.card == 'Q':
			string += 'Queen'
		elif self.card == 'K':
			string += "King"
		else:
			string += self.card

		string += " of "

		if self.suite == 'H':
			string += "Hearts"
		elif self.suite == 'D':
			string += "Diamonds"
		elif self.suite == 'C':
			string += "Clubs"
		else:
			string += "Spades"

		return string

	@staticmethod
	def getPoints(cardType, count):
		if cardType == 'R':
			return 50*count
		elif cardType == 'A' or cardType == '2':
			return 20*count
		elif cardType == 'K' or cardType == 'Q' or cardType == 'J' or cardType == '0':
			return 20*count
		elif cardType == '3':
			return -100
		else:
			return 5
