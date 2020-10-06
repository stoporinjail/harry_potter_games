from sys import exit as e

def Cedric_Diggory():
	while True:
		cedric_diggory = {"name":"Cedric Diggory",
						"species":"human",
						"gender":"male",
						"house":"Hufflepuff",
						"bloodStatus":"Unknown (not Muggle-born)",
						"eyeColor":"gray",
						"yrs_alive":"17",
						"parents":"Amos and Mrs. Diggory",
						"funFact":"He was killed as a 'spare'"
						}
		q1 = input('What do you want to learn about him? [N]ame, [S]pecies, [G]ender, [H]ouse, [B]lood status, [E]ye color, [Y]ears alive, [P]arents, or [F]un fact? ')
		if q1 == 'N':
			print(f'His name is {cedric_diggory["name"]}')
		elif q1 == 'S':
			print(f'His species is {cedric_diggory["species"]}')
		elif q1 == 'G':
			print(f'His gender is {cedric_diggory["gender"]}')
		elif q1 == 'H':
			print(f'His house is {cedric_diggory["house"]}')
		elif q1 == 'B':
			print(f'His blood status is {cedric_diggory["bloodStatus"]}')
		elif q1 == 'E':
			print(f'His eye color is {cedric_diggory["eyeColor"]}')
		elif q1 == 'A':
			print(f'He was {cedric_diggory["yrs_alive"]} years old (when he died)')
		elif q1 == 'P':
			print(f'His parents are {cedric_diggory["parents"]}')
		else:
			print(f'Here is a fun fact about him: {cedric_diggory["funFact"]}')
		q2 = input("What would you like to do? [L]earn more about him, [O]ther characters, or [E]xit the dictionary")
		if q2 == 'L':
			print("Loading, be patient...")
		elif q2 == 'O':
			print("Loading, be patient...")
			intro()
		else:
			print("Okay, exiting...")
			e(0)	
def Voldemort():
	while True:
		Voldemort = {"name":"Tom Marvolo Riddle Jr.",
					"species":"human (split soul)",
					"gender":"male",
					"house":"Slytherin",
					"bloodStatus":"half-blood",
					"eyeColor":"red (formerly brown)",
					"yrs_alive":"71 at death",
					"parents":"Merope and Tom Riddle Sr.",
					"funFact":"He and Harry's wand have a phoenix feather from the same phoenix"
					}
		q1 = input("What would you like to learn about Voldemort? [N]ame, [S]pecies, [G]ender, [H]ouse, [B]lood status, [E]ye color, [A]ge, [P]arents, or [F]un fact ")
		if q1 == 'N':
			print(f'His name is {Voldemort["name"]}')
		elif q1 == 'S':
			print(f'His species is {Voldemort["species"]}')
		elif q1 == 'G':
			print(f'His gender is {Voldemort["gender"]}')
		elif q1 == 'H':
			print(f'His house is {Voldemort["house"]}')
		elif q1 == 'B':
			print(f'His blood status is {Voldemort["bloodStatus"]}')
		elif q1 == 'E':
			print(f'His eye color is {Voldemort["eyeColor"]}')
		elif q1 == 'A':
			print(f'He is {Voldemort["yrs_alive"]} years old.')
		elif q1 == 'P':
			print(f'His parents are {Voldemort["parents"]}')
		else:
			print(f'Here is a fun fact about him: {Voldemort["funFact"]}')
		q2 = input("What would you like to do? [L]earn more about him, [O]ther characters, or [E]xit the dictionary")
		if q2 == 'L':
			print("Loading, be patient...")

		elif q2 == 'O':
			print("Loading, be patient...")
			intro()
		else:
			print("Okay, exiting...")
			e(0)
def Luna_Lovegood():
	while True:
		luna_lovegood = {"name":"Luna Lovegood",
						"species":"human",
						"gender":"female",
						"house":"ravenclaw",
						"bloodStatus":"half-blood",
						"eyeColor":"blue",
						"age":"39",
						"parents":"Pandora and Xenophilius Lovegood",
						"funFact":"Her father was trying to create the lost diadom of ravenclaw"}
		q1 = input("What do you want to learn about her? [N]ame, [S]pecies, [G]ender, [H]ouse, [B]lood status, [E]ye color, [A]ge, [P]arents, or [F]un fact?")
		if q1 == 'N':
			print(f'Her name is {luna_lovegood["name"]}')
		elif q1 == 'S':
			print(f'Her species is {luna_lovegood["species"]}')
		elif q1 == 'G':
			print(f'Her gender is {luna_lovegood["gender"]}')
		elif q1 == 'H':
			print(f'Her house is {luna_lovegood["house"]}')
		elif q1 == 'B':
			print(f'Her blood status is {luna_lovegood["bloodStatus"]}')
		elif q1 == 'E':
			print(f'Her eye color is {luna_lovegood["eyeColor"]}')
		elif q1 == 'A':
			print(f'She is {luna_lovegood["age"]} years old.')
		elif q1 == 'P':
			print(f'Her parents are: {luna_lovegood["parents"]}')
		else:
			print(f'Here is a fun fact about her: {luna_lovegood["funFact"]}')
		q2 = input('Would you like to [L]earn more about her, [O]ther characters, or [E]xit')
		if q2 == 'L':
			print("Okay, be patient.")
		elif q2 == 'O':
			print("Okay, be patient.")
			intro()
		else:
			print("Okay, be patient")
			e(0)
def Hermione_Granger():
	while True:
		hermione_granger = {"name":"Hermione Jean Granger",
							"species":"human",
							"gender":"female",
							"house":"gryffindor",
							"bloodStatus":"Muggle-born",
							"eyeColor":"brown",
							"age":"41",
							"parents":"Mrs. and Mr. Granger (names unknown)",
							"funFact":"Despite that she is very smart, the Sorting hat put her in Gryffindor"
							}
		q1 = input("What would you like to learn about Hermione Granger? [N]ame, [S]pecies, [G]ender, [H]ouse, [B]lood status, [E]ye color, [P]arents, [A]ge or [F]un fact\n\n")
		if q1 == 'N':
			print(f'Her full name is {hermione_granger["name"]}')
		elif q1 == 'S':
			print(f'Her species is {hermione_granger["species"]}')
		elif q1 == 'G':
			print(f'Her gender is {hermione_granger["gender"]}')
		elif q1 == 'H':
			print(f'Her house is {hermione_granger["house"]}')
		elif q1 == 'B':
			print(f'Her blood status is {hermione_granger["bloodStatus"]}')
		elif q1 == 'E':
			print(f'Her eye color is {hermione_granger["eyeColor"]}')
		elif q1 == 'P':
			print(f'Her parents are {hermione_granger["parents"]}')
		elif q1 == 'A':
			print(f'She is {hermione_granger["age"]} years old.')
		else:
			print(f'Here is a fun fact about her: {hermione_granger["funFact"]}')
		q2 = input("What would you like to do? [L]earn more about her, [O]ther characters, or [E]xit the dictionary")
		if q2 == 'L':
			print("Loading, be patient...")
		elif q2 == 'O':
			print("Loading, be patient...")
			intro()
		else:
			print("Okay, exiting...")
			e(0)
def Ron_Weasley():
	while True:
		ron_weasley = {"name":"Ronald Bilius Weasley",
					"species":"human",
					"gender":"male",
					"house":"Gryffindor",
					"bloodStatus":"Pure-blood",
					"eyeColor":"blue",
					"age":"40",
					"parents":"Molly and Arthur Weasley",
					"funFact":"Despite the fact that he doesn't speak parseltounge, he did it to open the chamber of secrets to get a basilisk fang in book 7."
					}

		q1 = input("What would you like to learn about Ron Weasley? [N]ame, [S]pecies [G]ender, [H]ouse, [B]lood Status, [E]ye Color, [P]arents, [A]ge or [F]un fact\n\n")
		if q1 == 'N':
			print(f'His full name is {ron_weasley["name"]}')
		elif q1 == 'S':
			print(f'His species is {ron_weasley["species"]}')
		elif q1 == 'G':
			print(f'His gender is {ron_weasley["gender"]}')
		elif q1 == 'H':
			print(f'His house is {ron_weasley["house"]}')
		elif q1 == 'B':
			print(f'His blood status is {ron_weasley["bloodStatus"]}')
		elif q1 == 'E':
			print(f'His eye color is {ron_weasley["eyeColor"]}')
		elif q1 == 'P':
			print(f'His parents are {ron_weasley["parents"]}')
		elif q1 == 'A':
			print(f'He is {ron_weasley["age"]} years old.')
		elif q1 == 'F':
			print(f'Here is a fun fact about him: {ron_weasley["funFact"]}')
		q2 = input("What would you like to do? [L]earn more about Ron, [Le]arn about other characters, or [E]xit this dictionary?")
		if q2 == 'L':
			print('Loading, this may take up to 7 seconds.')
		elif q2 == 'Le' or q2 == 'le' or q2 == 'LE':
			print("Loading, this may take up to 7 seconds.")
			intro()
			intro()
		else:
			e(0)
def Harry_Potter():
	while True:
		harry_potter = {"name":"Harry James Potter",
					"species":"human",
					"gender":"male",
					"house":"Gryffindor",
					"bloodStatus":"half-blood",
					"eyeColor":"green",
					"age":"40",
					"parents":"Lily and James Potter",
					"funFact":"Voldemort tried to kill him as a child, but didn't succeed. That left a scar on his forhead."
					}
		q2 = input("What would you like to learn about Harry Potter? [N]ame, [S]pecies [G]ender, [H]ouse, [B]lood Status, [E]ye Color, [P]arents, [A]ge or [F]un fact\n\n")
		if q2 == 'N':
			print(f'His full name is {harry_potter["name"]}')
		elif q2 == 'S':
			print(f'His species is {harry_potter["species"]}')
		elif q2 == 'G':
			print(f'His gender is {harry_potter["gender"]}')
		elif q2 == 'H':
			print(f'He is in {harry_potter["house"]}')
		elif q2 == 'B':
			print(f'He is {harry_potter["bloodStatus"]}')
		elif q2 == 'E':
			print(f'He has {harry_potter["eyeColor"]} eyes.')
		elif q2 == 'P':
			print(f'His parents are {harry_potter["parents"]}')
		elif q2 == 'F':
			print(f'Here is a fun fact about him: {harry_potter["funFact"]}')
		else:
			print(f'He is {harry_potter["age"]} years old.')
		q3 = input("Would you like to learn more about Harry Potter, about other characters, or exit this dictionary? [L]earn more about Harry Potter, [O]ther characters, or [E]xit ")
		if q3 == 'L' or q3 == 'l':
			print("Okay, loading, please be patient...")
		elif q3 == 'O' or q3 == 'o':
			print("Loading, please wait (it may take up to 7 seconds to load...")
			intro()
			intro()
	else:
		print("Bye, thanks for using this!")
		e(0)
def intro():
	q1 = input('Who would you like to learn about? [H]arry Potter, [R]on Weasley, [He]rmione Granger, [V]oldemort, [L]una Lovegood, [C]edric Diggory\n\n')
	if q1 == "H":
		print("Loading, please be patient.")
		Harry_Potter()
	elif q1 == 'R':
		Ron_Weasley()
	elif q1 == 'He' or q1 == 'he' or q1 == 'HE':
		Hermione_Granger()
	elif q1 == 'V' or q1 == 'v':
		Voldemort()
	elif q1 == 'L' or q1 == 'l':
		print("Loading, be patient")
		Luna_Lovegood()
	else:
		print("Loading...")
		Cedric_Diggory()	
intro()
