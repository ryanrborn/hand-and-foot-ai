# AIPlayer.py
# base class for ai players

import itertools
from Players.Player import Player
from Game.Card import Card

class AIPlayer(Player):
	"base class for ai players"

	@staticmethod
	def getOptions(hand, piles, requiredPoints):

		options = []
		typeOptions = []
		# options.append([]) # we need to give the option of doing nothing
		inPiles = {}
		notInPiles = {}
		wilds = {}
		# first let's split the cards we have in our hand into two different parts,
		# the cards that are in piles on the table, and the cards that aren't
		for handPile in hand.getTypes():
			# see if this is in piles
			if handPile == 'R' or handPile == '2':
				wilds[handPile] = hand.getCardCount(handPile)
			elif handPile in piles:
				inPiles[handPile] = hand.getCardCount(handPile)
			else:
				notInPiles[handPile] = hand.getCardCount(handPile)

		# now, have we already laid down the required amount?
		canLay = len(piles) > 0

		if canLay == True:
			# there are piles already on the table, do we have any we can lay down?
			if(len(inPiles) > 0):
				# sweet, we have some cards in our hand that are on the table, we can lay them down
				# give the option to lay down only one type, or all if more than one
				# TODO: give all options (if three cardTypes can be laid down, give options: [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3])
				for cardType, count in inPiles.iteritems():
					options.append([cardType])
					typeOptions.append(cardType)
			# any clean stuff?
			for cardType,count in notInPiles.iteritems():
				if count > 2:
					options.append([cardType])
					typeOptions.append(cardType)
			# now dirty
			# if 'R' in notInPiles or '2' in notInPiles:
			# 	# find sets of two and add wilds to them.
			# 	for cardType,count in notInPiles.iteritems():
			# 		if count == 2

			# can we sprinkle the wilds in?
			for cardType,count in wilds.iteritems():
				typeOptions.append(cardType)
			if len(typeOptions) >= 2:
				for i in range(2, len(typeOptions)+1):
					for x in itertools.combinations(typeOptions, i):
						option = list(x)
						if AIPlayer.isJustWilds(option):
							continue
						options.append(option)
		else:
			# we have to have enough points to lay down
			# first gather clean options
			cleanPoints = 0
			cleanOptions = []
			for cardType,count in notInPiles.iteritems():
				if count > 2 and cardType != 'R' and cardType != '2':
					cleanPoints += Card.getPoints(cardType, count)
					cleanOptions.append(cardType)

			# now gather dirty options



			if cleanPoints >= requiredPoints:
				canLay = True
				# cool, so we can lay down cleanly, let's add these to the options
				for cardType in preOptions:
					options.append([cardType])
					typeOptions.append(cardType)
			else:
				# still not enough points, do we have any wilds?
				if 'R' in notInPiles:
					points += Card.getPoints('R', notInPiles['R'])
				if '2' in notInPiles:
					points += Card.getPoints('2', notInPiles['R'])
				if points >= requiredPoints:
					canLay = True

			# can we lay now?




		# beforeLayOptions = []

		# # get options and points
		# cleanPoints = 0
		# cleanOptions = []
		# for cardType,count in notInPiles.iteritems():
		# 	if count > 2 and cardType != 'R' and cardType != '2':
		# 		cleanPoints += Card.getPoints(cardType, count)
		# 		cleanOptions.append(cardType)

		# if canLay == False:
		# 	if cleanPoints > requiredPoints:
		# 		# okay, so we haven't laid down, but we have enough cleanPoints to lay down
		# 		options.append(cleanOptions)
		# 		canLay = true
		# 	else:
		# 		# okay, we can't lay down cleanly, but do we have enough to lay down dirty?
		# 		if 'R' in notInPiles or '2' in notInPiles:
		# 			# we have wilds... iterate over cleanOptions
		# else:
		# 	# there are piles already on the table, we can put what we have into them
		# 	if(len(inPiles) > 0):
		# 		# yes, we have some cards in our hand that are on the table, we can lay them down
		# 		for cardType, count in inPiles.iteritems():
		# 			options.append(cardType)


		options.append([]) # we need to give the option of doing nothing

		print "number of options", len(options)
		print options
		for i in range(0,len(options)):
			print "option " + `i+1`
			for card in options[i]:
				print card+": "+`hand.getCardCount(card)`
			print ""
		# print options
		# print ""

	@staticmethod
	def isJustWilds(option):
		for x in option:
			if x != 'R' or x != '2':
				return False

		return True
