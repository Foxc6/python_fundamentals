import random
from random import randint

def randome_number():
	random.randint(60, 100)
	index = 0
	for i in range(0, 10):
		i = random.randint(60, 100)
		index = index + 1
		if i < 70:
			print "Score: " + str(i) + "; Your grade is D"
		if i > 69 and i < 80:
			print "Score: " + str(i) + "; Your grade is C"
		if i > 79 and i < 90:
			print "Score: " + str(i) + "; Your grade is B"
		if i > 89 and i <= 100:
			print "Score: " + str(i) + "; Your grade is A"

randome_number()
