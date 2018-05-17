my_list = ["A","b", "Hello", "World"]
def list_type(my_list):
	new_string = ""
	total = 0
	has_string = False
	has_int = False
	message1 = "The list you entered is of string type"
	message2 = "The list you entered is of integer type"
	message3 = "The list you entered is of mixed type"
	for val in my_list:
		if isinstance(val, str):
			new_string += val
			has_string = True
		if isinstance(val, int):
			total = total + val
			has_int = True
	if has_string == True and has_int == False:
		print message1
		print new_string
	if has_string == False and has_int == True:
		print message2
		print total
	if has_string == True and has_int == True:
		print message3
		print new_string
		print total

list_type(my_list)