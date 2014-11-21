# Human.py
# a human player

class Human(Player):

	def draw(self, draw):
		for d in draw:
			hand.append(d)

	def laydown(self, safe, discard):
		# ask the user what they are laying down
		print "Please list all of the cards you are laying down hitting enter for each card: K D or 10 H"
		print "K = King"
		print "Q = Queen"
		print "J = Jack"
		print "R = Joker"
		print "H = Hearts"
		print "D = Diamonds"
		print "C = Clubs"
		print "S = Spades"
		print "Q = Done"

		while True:
			inp = raw_input("Card: ")
			if(inp == "Q" or inp == "q"):
				break;
			parts = inp.split(" ")
			if(parts[0] == "K" or parts[0] == "k"):




	def isItSafe(self):
		# get input from user as to the answer
