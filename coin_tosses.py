import random
from random import randint

def coin_toss():
	heads = 0
	tails = 0
	index = 1
	for i in range(0, 5000):
		i = random.randint(0, 1)
		if i == 0:
			heads = heads + 1
			print "Attempt #" + str(index) + ": Throwing a coin... It's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
			index = index + 1
		elif i == 1:
			tails = tails + 1
			print "Attempt #" + str(index) + ": Throwing a coin... It's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
			index = index + 1
	print "Ending the program, thank you!"

coin_toss()