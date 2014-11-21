# DeckFactory.py
# creates arrays of Cards that constitutes a deck

import Card

class DeckFactory:
	"Creates an array of Cards that constitutes a deck"

	@staticmethod
	def createDeck(self, numDecks=1):
		deck = []
		for i in range(numDecks):
			# first we create the jokers
			for j in range(2):
				deck.append(Card.Card('','R'))

			# now we loop through the suites and cards
			suites = ['H','D','C','S']
			cards = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
			for s in suites:
				for c in cards:
					deck.append(Card.Card(s,c))

		return deck