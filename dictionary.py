me = {
"name": "Chris Fox",
"age": 32,
"country_of_birth": "The United States of America",
"favorite_language": "Ruby"
}

def dictionary(obj):
	print "My name is " + obj["name"]
	print "My age is " + str(obj["age"])
	print "My County of Birth is " + obj["country_of_birth"]
	print "My Favorite Language is " + obj["favorite_language"]

dictionary(me)