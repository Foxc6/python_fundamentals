person = {
	"first_name": "Chris",
	"last_name": "Fox",
	"age": 32,
	"email": "foxc6@hotmail.com"
}

person["school"] = "Coding Dojo"

print person

print person["school"]

for data in person:
    print data

for values in person.itervalues():
	print values

print person.values()

