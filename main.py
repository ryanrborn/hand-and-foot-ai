#! /usr/bin/env python
# Ryan Born
# Hand and Foot AI
# Dr. Flann

import random

from Game.DeckFactory import DeckFactory
from Players.AI.RandomBot import RandomBot

deck = DeckFactory.createDeck(1)

random.shuffle(deck)

# get hand and foot for our Player

hand = []
foot = []
for i in range(12):
	hand.append(deck.pop())
	foot.append(deck.pop())

steve = RandomBot("steve", hand, foot)

steve.laydown([4,6], False, [], 50)