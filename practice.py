# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
def find_replace(words):
	print words.find('day')
	new = words.replace("day", "month")
	print new

find_replace(words)


#Min and Max
num_arr = [2,54,-2,7,12,98]
def min_max(num_arr):
	print min(num_arr)
	print max(num_arr)

min_max(num_arr)


#First and Last
initial_list = ["hello",2,54,-2,7,12,98,"world"]
def first_last(initial_list):
	first = initial_list[0]
	print first
	last = initial_list[len(initial_list) -1]
	print last
	new_string = first + last
	print (new_string)

#New List
my_list = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
def new_list(my_list):
	my_list.sort()
	halfway = len(my_list)/2
	first_half = my_list[:halfway]
	for i in range(0, halfway):
		my_list.pop(0)
	my_list.insert(0, first_half)
	print my_list

new_list(my_list)

