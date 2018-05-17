students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def return_students(arr):
	index = 0
	temp_arr = []
	for obj in arr:
		obj = arr[index]
		index += 1
		for values in obj.values():
			temp_arr.append(values)
		print temp_arr[0], temp_arr[1]
		temp_arr = []

return_students(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def return_students(obj):
	print "Students"
	index = 0
	temp_arr = []
	students = users["Students"]
	instructors = users["Instructors"]
 	for arr in students:
		arr = students[index]
		index += 1
		for values in arr.values():
			temp_arr.append(values)
		count1 = len(temp_arr[0])
		count2 = len(temp_arr[1])
		total = count1 + count2
		print index, "-", temp_arr[0], temp_arr[1], "-", total
		temp_arr = []

	print "Instructors"
	index = 0
	for arr in instructors:
		arr = instructors[index]
		index += 1
		for values in arr.values():
			temp_arr.append(values)
		count1 = len(temp_arr[0])
		count2 = len(temp_arr[1])
		total = count1 + count2
		print index, "-", temp_arr[0], temp_arr[1], "-", total
		temp_arr = []

return_students(users)


# The solution below is much simpler
'''def show_students(arr):
    for student in students:
        print student['first_name'], student['last_name']

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)

show_students(students)
show_all(users)'''


