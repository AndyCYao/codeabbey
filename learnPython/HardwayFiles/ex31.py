print("You enter a dark room with two doors, " + 
	" do you go through door 1 or door 2?")

door = str(input("> "))

if door == "1":
	print("There's a giant bear here eating a cheese" + 
		"cake, what do you want to do?")
	print("1. take the cake")
	print("2. scream at the bear")

	bear = str(input("> "))

	if bear == "1":
		print("the bear eats your face off, good job")
	elif bear == "2":
		print("the bear eats your leg off, good job")
	else:
		print ("well, doing %s is prob better, bear " +
			"run's away" %(bear))
elif door == "2":
	print("you stare into the endless abyss at cthulu retina")
	print("1. blueberries")
	print("2. yellow jacket clothspins")
	print("3. understanding revolvers yeling melodies")

	insanity = str(input("> "))

	if insanity == "1" or insanity == "2":
		print("your body survives powered by a mind of " +
			" jello, good job")
	else:
		print("the insanity rots your eyes into a pool of mnuch")
else:
	print("you stumbled around and fall on a knife and die")