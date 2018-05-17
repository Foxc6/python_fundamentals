name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(key, val):
	dictionary = dict(zip(key, val))
	print dictionary

make_dict(name, favorite_animal)