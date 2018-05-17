values = ['hello','world','my','name','is','Anna']
char = 'o'
def find_characters(values, char):
	new_list = []
	index = 0
	for i in values:
		val = values[index]
		if char in val: 
			index = index + 1
			new_list.append(val)
		else:
			index = index + 1
			continue
	print new_list

find_characters(values, char)