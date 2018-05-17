# Multipes
# Part 1: Write code that prints all the odd numbers from 1 to 1000.
def odd_numbers():
	for i in range(1, 1000):
		if i%2 != 0:
			print i

odd_numbers()

# Part 2: Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def multiples():
	for i in range(1, 1000000):
		if i%5 == 0:
			print i

multiples()

# Sum List: Print out the sum of a list of numbers.
sum_list = [1, 2, 5, 10, 255, 3]
def total_sum(sum_list):
	length = len(sum_list)
	total = 0
	for index in range(0, length):
		total = total + sum_list[index]
	print total
total_sum(sum_list)

#Average List: print out the average of a list of numbers.
average_list = [1, 2, 5, 10, 255, 3]
def total_average():
	length = len(average_list)
	total = 0
	for index in range(0, length):
		total = total + sum_list[index]
	average = total / length
	print average
total_average()
