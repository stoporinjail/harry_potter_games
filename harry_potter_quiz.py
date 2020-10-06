from sys import exit as e
name = input('What is your name? ')
def dictionary():
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
			if q1 == 'N' or q1 ==  'n':
				print(f'His name is {cedric_diggory["name"]}')
			elif q1 == 'S' or 's':
				print(f'His species is {cedric_diggory["species"]}')
			elif q1 == 'G' or q1 == 'g':
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
			if q2 == 'N' or q2 == 'n':
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

def Luna_Lovegood():
	status = True
	while status:
		correct = 0
		wrong = 0
		Luna_Lovegood = {}
		q1 = input(f"{name.title()}, what is Luna's species? ")
		if q1 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["species"] = q1
		q2 = input(f"{name.title()}, what is Luna's gender? ")
		if q2 == 'female' or 'Female':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["gender"] = q2
		q3 = input(f"{name.title()}, what is Luna's house? ")
		if q3 == 'ravenclaw' or 'Ravenclaw':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["house"] = q3
		q4 = input(f"{name.title()}, what is Luna's blood status? ")
		if q4 == 'half-blood' or 'Half blood' or 'Half Blood' or 'Half-blood' or 'Half-Blood':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["blood status"] = q4
		q5 = input(f"{name.title()}, what is Luna's age? ")
		if q5 == '39' or 'thirty-nine' or 'thirty nine':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["age"] = q5
		q6 = input(f"{name.title()}, what are Luna's parents names? ")
		if q6 == 'pandora and xenophilius lovegood' or 'Pandora and Xenophilius Lovegood' or 'Xenophilius and Pandora Lovegood' or 'xenophilius and pandora lovegood':
			correct += 1
		else:
			wrong += 1
		Luna_Lovegood["parents"] = q6
		for key, value in Luna_Lovegood.items():
			print(f'Here is what you put in for {key}: {value}')
		q7 = input('Is this correct? ')
		if q7 == 'yes' or 'Yes' or 'y' or 'Y':
			print('Good, here are your results:')
			print(f'You got {correct} out of 6')
		else:
			print('Try again, start over this quiz.')
		q8 = input('It is the end, would you like to learn about these characters (no quiz)? y/n ')
		if q8 == 'y' or 'Y':
			dictionary()
		else:
			e('Okay, exiting.')	
		# Questions: Name, species, gender, house, blood status, eye color, age, parents.
def Cedric_Diggory():
	status = True
	while status:
		correct = 0
		wrong = 0
		Cedric_Diggory = {}
		q1 = input(f"{name.title()}, what is Cedric's species? ")
		if q1 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["species"] = q1 
		q2 = input(f"{name.title()}, what is Cedric's gender? (answer either female or male) ")
		if q2 == 'male' or 'Male':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["gender"] = q2
		q3 = input(f"{name.title()}, what is Cedric's house? ")
		if q3 == 'hufflepuff' or 'Hufflepuff':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["house"] = q3
		q4 = input(f"{name.title()}, what is Cedric's blood status? ")
		if q4 == 'half-blood' or 'Half-blood' or 'Half-Blood' or 'half blood' or 'Half blood' or 'Half Blood':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["blood status"] = q4
		q5 = input(f"{name.title()}, what is Cedric's eye color? ")
		if q5 == 'gray' or 'Gray' or 'grey' or 'Grey':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["eye color"] = q5
		q6 = input(f"{name.title()}, what was Cedric's age (at death) ")
		if q6 == '17' or 'seventeen' or 'Seventeen' or 'seven teen' or 'Seven teen' or 'Seven Teen' or 'seven-teen' or 'Seven-Teen' or 'Seven-teen':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["age"] = q6
		q7 = input(f"{name.title()}, what is Cedric's dad's name? ")
		if q7 == 'Amos Diggory' or 'amos diggory' or 'Amos diggory' or 'amos Diggory':
			correct += 1
		else:
			wrong += 1
		Cedric_Diggory["parents"] = q7
		print(F"{name.title()}, that is the end. Note: Since Cedric's mother's name is unknown and Cedric doesn't have a middle name/middle name unknown, there will be no question on that.")
		print('Here is what you put in earlier, you will get a confirmation message.')
		for key, value in Cedric_Diggory.items():
			print(f'\tHis {key} is {value}\n')
		Cedric_Diggory_correct = {"species":"human",
									"gender":"male",
									"house":"Hufflepuff",
									"blood status":"half-blood",
									"eye color":"gray",
									"age":"17",
									"parents":"Amos Diggory, mother name unknown"}
		print(f"Here are your results:\nYou got {correct} correct and {wrong} wrong out of 7")
		print('Here are the correct answers:')
		for key, value in Cedric_Diggory_correct.items():
			print(f'\tHis {key} is {value}\n')
		q8 = input(f"{name.title()}, would you like to do the last quiz, or do this again? [L]ast quiz, [D]o this again ")
		if q8 == 'l' or 'L':
			Luna_Lovegood()


# Questions: Name, species, gender, house, blood status, eye color, age, parents.
def Voldemort():
	status = True
	while status:
		correct = 0
		wrong = 0
		voldemort = {}
		q1 = input(f"{name.title()}, what is Voldemort's real and full name? ")
		if q1 == 'tom marvolo riddle' or 'Tom marvolo riddle' or 'Tom Marvolo Riddle' or 'Tom marvolo Riddle':
			correct += 1
		else:
			wrong += 1
		voldemort["name"] = q1
		q2 = input(f"{name.title()}, what is Voldemort's species? ")
		if q2 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		voldemort["species"] = q2
		q3 = input(f"{name.title()}, what is Voldemort's gender?")
		if q3 == 'male' or 'Male':
			correct += 1
		else:
			wrong += 1
		voldemort["gender"] = q3
		q4 = input(f"{name.title()}, what is Voldemort's house? ")
		if q4 == 'Slytherin' or 'slytherin':
			correct += 1
		else:
			wrong += 1
		voldemort["house"] = q4
		q5 = input(f"{name.title()}, what is Voldemort's blood status? ")
		if q5 == 'half blood' or 'Half Blood' or 'Half blood' or 'half Blood' or 'Half-Blood' or 'Half-blood' or 'half-blood':
			correct += 1
		else:
			wrong += 1
		voldemort["blood status"] = q5
		q6 = input(f"{name.title()}, what is Voldemort's eye color? ")
		if q6 == 'red' or 'Red':
			correct += 1
		else:
			wrong += 1
		voldemort["eye color"] = q6
		q7 = input(f"{name.title()}, what is Voldemort's age (at death)? ")
		if q7 == '71' or 'seventy-one' or 'Seventy-One' or 'Seventy-one' or 'Seventy one' or 'Seventy one' or 'Seventy One':
			correct += 1
		else:
			wrong += 1
		voldemort["age"] = q7
		q8 = input(f"{name.title()}, what are Voldemort's parent's names? ")
		if q8 == 'Merope and Tom Riddle' or 'merope and tom riddle' or 'Merope and Tom riddle' or 'Merope And Tom Riddle' or 'Tom and Merope Riddle' or 'tom and merope riddle':
			correct += 1
		else:
			wrong += 1
		voldemort["parents"] = q8
		print(f'Here is what you put in earlier. You will get a confirmation message. ')
		for key, value in voldemort.items():
			print(f'\tHis {key} is {value}.\n')
		print(f'Here are your results:\nYou got {correct} right and {wrong} wrong out of 8.')
		voldemort_correct_answers = {"name":"Tom Marvolo Riddle",
									"species":"human",
									"gender":"male",
									"house":"Slytherin",
									"blood status":"half-blood",
									"eye color":"red",
									"age":"71 at death",
									"parents":"Merope and Tom Riddle"
									}
		print('here are the correct answers:')
		for key, value in voldemort_correct_answers.items():
			print(f'His {key} is {value}')
		q0 = input(f"{name.title()}, what would you like to do? [D]o this again, or [N]ext quiz? ")
		if q0 == 'N' or 'n':
			Cedric_Diggory()
		# Questions: Name, species, gender, house, blood status, eye color, age, parents.
def hermione_granger():
	status = True
	while status:
		correct = 0
		wrong = 0
		hermione_granger = {}
		q1 = input(f'{name.title()}, what is Hermione' + "'s full name? ")
		if q1 == 'Hermione Jean Granger' or 'Hermione jean granger' or 'hermione jean granger':
			correct += 1
		else:
			wrong += 1
		hermione_granger["name"] = q1
		q2 = input(f"{name.title()}, what is Hermione's species? ")
		if q2 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		hermione_granger["species"] = q2 
		q3 = input(f"{name.title()}, what is Hermione's gender? ")
		if q3 == 'female' or 'Female' or 'girl' or 'Girl' or 'woman' or 'Woman':
			correct += 1
		else:
			wrong += 1
		hermione_granger["gender"] = q3
		q4 = input(f"{name}, what is Hermione's house? ")
		if q4 == 'gryffindor' or 'Gryffindor':
			correct += 1
		else:
			wrong += 1
		hermione_granger["house"] = q4
		q5 = input(f"{name.title()}, what is Hermione's blood status? ")
		if q5 == 'Muggle Born' or 'muggle born' or 'Muggle born' or 'muggle-born' or 'Muggle-Born' or 'Muggle-born':
			correct += 1
		elif q5 == 'mudblood' or 'Mudblood' or 'mud blood' or 'Mud Blood' or 'Mud blood':
			print(f"{name}, that is very offensive, you may not continue!".upper())
			e(0)
		else:
			wrong += 1
		hermione_granger["blood status"] = q5
		q6 = input(f"{name.title()}, what is Hermione's eye color? ")
		if q6 == 'brown' or 'Brown':
			correct += 1
		else:
			wrong += 1
		hermione_granger["eye color"] = q6
		q7 = input(f"{name.title()}, what is Hermione's age? ")
		if q7 == '41' or 'forty one' or 'Forty one' or 'Forty One' or 'forty-one' or 'Forty-one' or 'Forty-One':
			correct += 1
		else:
			wrong += 1
		hermione_granger["age"] = q7
		print(f'{name.title()}, that was the last question. NOTE: Since Hermione' + "'s parent's names are unknown, I will not do a question on them.")
		print("Here is what you put in earlier:")
		for key, value in hermione_granger.items():
			print(f'\tHer {key} is {value}.\n')
		print(f'Here are your results:\nYou got {correct} right and {wrong} wrong out of 7.')
		hermione_granger_correct_answers = {"name":"Hermione Jean Granger",
											"species":"human",
											"gender":"female",
											"house":"Gryffindor",
											"blood status":"muggle-born",
											"eye color":"brown",
											"age":"41"
											}
		print('Here are the correct answers:\n')
		for key, value in hermione_granger_correct_answers.items():
			print(f'\tHer {key} is {value}.\n')
		q10 = input(f"{name.title()}, what would you like to do? [D]o this quiz again, or [N]ext quiz? ")
		if q10 == 'N' or 'n':
			Voldemort()
# Questions: Name, species, gender, house, blood status, eye color, age, parents.
def ron_Weasley():
	status = True
	wrong = 0 
	correct = 0
	while status:
		# Questions: Name, species, 		
		ron_Weasley = {}
		q1 = input(f"What is Ron's full name? ")
		if q1 == 'ron bilius weasley' or 'Ron Bilus Weasley':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["name"] = q1
		q2 = input(F"{name.title()}, what is Ron's species? ")
		if q2 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["species"] = q2
		q3 = input(f"{name.title()}, what is Ron's gender? ")
		if q3 == 'male' or 'Male' or 'boy' or 'Boy' or 'man' or 'Man':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["gender"] = q3
		q4 = input(f"{name.title()}, what is Ron's house? ")
		if q4 == 'gryffindor' or 'Gryffindor':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["house"] = q4
		q5 = input(f"{name.title()}, what is Ron's blood status? ")
		if q5 == 'pure blood' or 'Pure Blood' or 'Pure blood' or 'Pure-blood' or 'pure-blood' or 'pureblood':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["blood status"] = q5
		q6 = input(f"{name.title()}, what is Ron's eye color? ")
		if q6 == 'blue' or 'Blue':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["eye color"] = q6
		q7 = input(f"{name.title()}, what is Ron's age? ")
		if q7 == '40' or 'forty' or 'Forty':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["age"] = q7
		q8 = input(f"{name.title()}, what are Ron's parents? ")
		if q8 == 'Molly and Arthur Weasley' or 'molly and arthur weasley' or 'Molly and arthur weasley' or 'arthur and molly Weasley' or 'Arthur and Molly Weasley':
			correct += 1
		else:
			wrong += 1
		ron_Weasley["parents"] = q7
		print("What you put in will appear shortly.")
		for key, value in ron_Weasley.items():
			print(f'\tHis {key} is {value}\n')
		q9 = input(f'{name.title()}, is this info correct? y/n ')
		if q9 == 'y':
			print("Awesome, here are the results:")
		else:
			print(f'{name.title()}, try again. ')
			status = False
		print(f'You got {correct} correct and {wrong} wrong out of 8.')
		ron_Weasley_correct_answers = {"name":"Ron james Weasley",
										"species":"human",
										"gender":"male",
										"house":"Gryffindor",
										"blood status":"pure-blood"}
		print('Here are the correct answers:')
		for key, value in ron_Weasley_correct_answers.items():
			print(f'His {key} is {value}.\n\t')
		q10 = input(f'What would you like to do? [D]o the quiz again, or [N]ext quiz? ')
		if q10 == 'N' or 'n':
			hermione_granger()
def harry_potter():
	status = True
	correct = 0
	wrong = 0
	while status:
		Harry_Potter = {}
		# Questions: Name, species, gender, house, blood status, eye color, age, parents.
		q1 = input(f"What is Harry's full name? ")
		if q1 == 'Harry James Potter':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["name"] = q1
		q2 = input(F"{name.title()}, what is Harry's species? ")
		if q2 == 'human' or 'Human':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["species"] = q2
		q3 = input(f"{name.title()}, what is Harry's gender? ")
		if q3 == 'male' or 'Male' or 'boy' or 'Boy' or 'man' or 'Man':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["gender"] = q3
		q4 = input(f"{name.title()}, what is Harry's house? ")
		if q4 == 'gryffindor' or 'Gryffindor':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["house"] = q4
		q5 = input(f"{name.title()}, what is Harry's blood status? ")
		if q5 == 'pure blood' or 'Pure Blood' or 'Pure blood' or 'Pure-blood' or 'pure-blood' or 'pureblood':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["blood status"] = q5
		q6 = input(f"{name.title()}, what is Harry's eye color? ")
		if q6 == 'blue' or 'Blue':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["eye color"] = q6
		q7 = input(f"{name.title()}, what is Harry's age? ")
		if q7 == '40' or 'forty' or 'Forty':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["age"] = q7
		q8 = input(f"{name.title()}, what are Harry's parents? ")
		if q8 == 'James and Lily Potter':
			correct += 1
		else:
			wrong += 1
		Harry_Potter["parents"] = q7
		print("What you put in will appear shortly.")
		for key, value in Harry_Potter.items():
			print(f'\tHis {key} is {value}\n')
		q9 = input(f'{name.title()}, is this info correct? y/n ')
		if q9 == 'y':
			print("Awesome, here are the results:")
		else:
			print(f'{name.title()}, try again. ')
			status = False
		print(f'You got {correct} correct and {wrong} wrong out of 8.')
		Harry_Potter_correct_answers = {"name":"Harry James Potter",
										"species":"human",
										"gender":"male",
										"house":"Gryffindor",
										"blood status":"half-blood"}
		print('Here are the correct answers:')
		for key, value in Harry_Potter_correct_answers.items():
			print(f'His {key} is {value}.\n\t')
		q10 = input(f'What would you like to do? [D]o the quiz again, or [N]ext quiz? ')
		if q10 == 'N' or 'n':
			ron_Weasley()
harry_potter()
