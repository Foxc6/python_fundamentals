line_a = "* * * * "
line_b = " * * * *"
rows = 8

def checkerboard(line_a, line_b):
	index = 1
	for r in range(1, rows+1):
		if index % 2 != 0:
			print line_a
			index = index + 1
		else: 
			print line_b
			index = index + 1

checkerboard(line_a, line_b)