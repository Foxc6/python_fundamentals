# Odd/Even

def odd_even():
	for i in range(1, 2001):
		if i % 2 != 0:
			print "Number is " + str(i) + ". This is an odd number!"
		else:
			print "Number is " + str(i) + ". This is an even number!"

odd_even()

# Multiply

num_list = [1, 2, 3, 4, 5,]
mult = 2

def multiply(num_list, mult):
	index = 0
	temp_list = []
	for i in range(index, len(num_list)):
		temp_list.append(num_list[i] * mult)
		index = index + 1
	return temp_list
	print temp_list

multiply(num_list, mult)

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

