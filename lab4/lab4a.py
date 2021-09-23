def split_it(message):


	firstPart = ""
	secondPart = ""
	for i in list(message):
		if i == "_" or i == "." or i.islower():
			firstPart += i
		if i == " " or i == "|" or i.isupper():
			secondPart += i
		else:
			pass
	return firstPart, secondPart





def split_rec(message):
	message = list(message)
	if len(message) == 0:

		return ("","")

	if message[0] == "_" or message[0] == "." or message[0].islower():
		(firstPart,secondPart) = split_rec(message[1:])
		return (message[0]+ firstPart, secondPart)

	elif message[0] == " " or message[0] == "|" or message[0].isupper():
		(firstPart,secondPart) = split_rec(message[1:])
		return (firstPart, message[0] + secondPart)
	else:
		return split_rec(message[1:])



