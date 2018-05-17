arr = ["abcd",3,6,4,8,2,"efghijklmnop",10]
def draw_stars(arr):
	index = 0
	for i in arr:
		if isinstance(arr[index], int):
			print "*" * arr[index]
			index = index + 1
		elif isinstance(arr[index], str):
			print (arr[index][0]) * len(arr[index])
			index = index + 1

draw_stars(arr)

