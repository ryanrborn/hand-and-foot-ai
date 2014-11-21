# Pile.py
# simple pile of cards

class Pile:

	def __init__(self):
		self.cards = []
		self.cardType = ''
		self.wildCount = 0
		self.closed = False

	def setType(self, type):
		self.cardType = type

	def getType(self):
		return self.cardType

	def isClosed(self):
		return self.closed

	def addCard(self, card):
		if card.getCard() == 'R' and self.canAddWild() == False:
			print "sorry, can't have more wilds than real cards in a pile"
			return;
		if card.getCard() == self.cardType:
			self.cards.append(card)
		elif card.getCard() == 'R':
			self.cards.append(card)
			self.wildCount++
		if len(self.cards) == 7:
			self.closed = True

	def canAddWild(self):
		if self.wildCount+1 <= len(self.cards)/2:
			return True;
		return False;