import random
import time
import sys
def Sorting_Hat():
	age = input(F"{name}, how old are you? ")
	age = int(age)
	if age != 11:
		if age > 11:
			if age == 12 or 13 or 14 or 15 or 16 or 17:
				print(f"Go to your house table, {name.title()}, you are already sorted.")
				sys.exit('Already sorted.')
			elif age > 17:
				print(f"You are not attending Hogwarts any more, {name.title()}...Why are you here?")
				sys.exit('Out of school, not attending Hogwarts.')
		elif age < 11:
			print(f"You are too young, {name.title()}. Come back when you are 11 years old.")
			sys.exit['Too young.']
	Gryffindor = 0
	Hufflepuff = 0
	Ravenclaw = 0
	Slytherin = 0
	Q1 = input (F' {name.title()}, there are four houses. [R]avenclaw, [H]ufflepuff, [G]ryffindor, and [S]lytherin. Which of these do you like? ')
	if Q1 == "R":
		Ravenclaw += 1
	elif Q1 == "H":
		Hufflepuff += 1
	elif Q1 == "G":
 		Gryffindor += 1
	elif Q1 == "S":
 		Slytherin += 1
	Q2 = input(F' {name.title()}, is your name Tom Riddle? y/n ')
	if Q2 == "y":
  		sys.exit("Please leave the school, you are not allowed entrance. ")
	Q3 = input(F"What do you like to do the most on a wand? A. Unforgiveable curses. B. Charms. C. Tranfiguration. D. A variety. ")
	if Q3 == "A":
 		Slytherin += 2
	elif Q3 == "B":
		Ravenclaw += 2
		Hufflepuff += 2
	elif Q3 == "C":
		Gryffindor += 2
	else:
		Ravenclaw += 2
	time.sleep(0.5)
	Q4 = input(F'{name.title()}, what is your favorite animal? [B]adger, [S]nake, [L]ion, [E]agle. ')
	if Q4 == "B":
		Hufflepuff += 2
	elif Q4 == "S":
		Slytherin += 2
	elif Q4 == "L":
		Gryffindor += 2
	else:
		Ravenclaw += 2	
	Q5 = input(f"{name.title()}, who is your favorite character in Harry potter out of these: A. Harry. B. Luna. C. Cedric. D. Draco ")
	if Q5 == "A":
		Gryffindor+=2
	elif Q5 == "B":
		Ravenclaw += 2
	elif Q5 == "C":
		Hufflepuff += 2
	else:
		Slytherin += 2
	Q6 = input(F"{name.title()} Are you: A. ambitious, B. Loyal. C. Brave, or D. Smart? ")
	if Q6 == "A":
		Slytherin += 2
	elif Q6 == "B":
		Hufflepuff += 2
	elif Q6 == "C":
		Gryffindor += 2
	else:
		Ravenclaw += 2
	Q7 = input(F"{name.title()}, what would you do if you were being chased by a werewolf? [F]ight, [R]un, or [P]anic? ")
	if Q7 == "F":
		Gryffindor+=5
	else:
		Slytherin += 1
		Hufflepuff +=1
		Ravenclaw+=1
	Q8 = input(f'{name.title()}Would you rather: [G]et a bad grade, [S]urrender, [B]etray someone, or [N]ot get what you want ')
	if Q8 == "G":
		Ravenclaw -= 2
	elif Q8 == "S":
		Gryffindor -= 2
	elif Q8 == "B":
		Hufflepuff -= 2
	else:
		Slytherin -= 2
	time.sleep(0.5)
	print("That's the end! Give me a moment to calculate your results!")
	time.sleep(1.5)
	if Gryffindor != Ravenclaw and Hufflepuff and Slytherin:
		if Gryffindor > Ravenclaw and Gryffindor > Slytherin and Gryffindor > Hufflepuff:
			print("Congratulations, you are in Gryffindor!")

		elif Ravenclaw > Gryffindor and Ravenclaw > Slytherin and Ravenclaw > Hufflepuff:
			print("Congratulations, you are in Ravenclaw!")

		elif Slytherin > Ravenclaw and Slytherin > Gryffindor and Slytherin > Hufflepuff:
			print("Congratulations, you are in Slytherin!")

		else:
			print("Congratulations, you are in Hufflepuff!")

	elif Gryffindor == Ravenclaw and Gryffindor == Slytherin and Gryffindor == Hufflepuff and Ravenclaw == Hufflepuff and Ravenclaw == Slytherin and Hufflepuff == Slytherin:
			print("You have been chosen for all of the houses. Choose which one yourself.")
	elif Hufflepuff == Gryffindor and Hufflepuff == Ravenclaw and Ravenclaw and Gryffindor and Hufflepuff > Slytherin:
			h1 = input (f' You have been chosen for 3 houses {name}, which do you prefer, [H]ufflepuff, [R]avenclaw, or [G]ryffindor? ')
			if h1=='H':
				print('Congratulations, you are in Hufflepuff!')
			elif h1=='R':
				print('Congratulations, you are in Ravenclaw!')
			else:
				print('Congratulations, you are in Gryffindor!')

	elif Hufflepuff == Gryffindor and Hufflepuff == Slytherin and Hufflepuff and Slytherin and Gryffindor > Ravenclaw:
			h2 = input (f' You have been chosen for 3 houses {name}, which do you prefer, [H]ufflepuff, [S]lytherin, or [G]ryffindor? ')
			if h2=='H':
				print('Congratulations, you are in Hufflepuff!')
			elif h2=='S':
				print('Congratulations, you are in Slytherin!')
			else:
				print('Congratulation, you are in Gryffindor!')

	elif Hufflepuff == Ravenclaw and Hufflepuff == Slytherin and Slytherin and Ravenclaw and Hufflepuff > Gryffindor:
			h3 = input (f' You have been chosen for 3 houses {name}, which do you prefer, [H]ufflepuff, [S]lytherin, or [R]avenclaw? ')
			if h3=='H':
				print('Congratulations, you are in Hufflepuff!')
			elif h3=='S':
				print('Congratulations, you are in Slytherin!')
			else:
				print('Congratulations, you are in Ravenclaw!')

	elif Ravenclaw == Gryffindor and Ravenclaw == Slytherin and Ravenclaw and Gryffindor and Slytherin > Hufflepuff:
		h4 = input (f' You have been chosen for 3 houses {name}, which do you prefer, [R]avenclaw, [S]lytherin, or [G]ryffindor? ')
		if h4=='R':
			print('Congratulations, you are in Ravenclaw!')
		elif h4=='S':
			print('Congratulations, you are in Slytherin!')
		else:
			print('Congratulation, you are in Gryffindor!')

	elif Gryffindor == Hufflepuff and Gryffindor > Ravenclaw and Slytherin and Hufflepuff > Ravenclaw and Slytherin:
		jl = input (f' You have been chosen for 2 houses {name}, which do you prefer, [H]ufflepuff or [G]ryffindor? ')
		if jl=='H':
			print('Congratulations, you are in Hufflepuff!')
		else:
			print('Congratulations, you are in Gryffindor!')

	elif Gryffindor == Slytherin and Slytherin > Ravenclaw and Hufflepuff and Gryffindor > Ravenclaw and Hufflepuff:
		j2 = input (f' You have been chosen for 2 houses {name}, which do you prefer, [S]lytherin or [G]ryffindor? ')
		if (j2=='S'):
			print('Congratulations, you are in Slytherin!')
		else:
			print('Congratulations, you are in Gryffindor!')

	elif Gryffindor == Ravenclaw and Gryffindor > Hufflepuff and Slytherin and Ravenclaw > Hufflepuff and Slytherin:
		j3 = input (f' You have been chosen for 2 houses {name}, which do you prefer, [R]avenclaw or [G]ryffindor? ')
		if j3=='R':
			print('Congratulations, you are in Ravenclaw!')
		else:
			print('Congratulations, you are in Gryffindor!')
	elif Ravenclaw == Hufflepuff and Hufflepuff > Gryffindor and Slytherin and Ravenclaw > Gryffindor and Slytherin:
		j4 = input (f' You have been chosen for 2 houses {name}, which do you prefer, [R]avenclaw or [H]ufflepuff? ')
		if j4=='R':
			print('Congratulations, you are in Ravenclaw!')
		else:
			print('Congratulations, you are in Hufflepuff!')

	elif Ravenclaw == Slytherin and Ravenclaw > Gryffindor and Hufflepuff and Slytherin > Gryffindor and Hufflepuff:
		j5 = input (f' You have been chosen for 2 houses {name}, which do you prefer, [S]lytherin or [R]avenclaw? ')
		if j5=='S':
			print('Congratulations, you are in Slytherin!')
		else:
			print('Congratulations, you are in Ravenclaw!')

	elif Hufflepuff == Slytherin and Hufflepuff > Ravenclaw and Hufflepuff > Gryffindor and Slytherin > Ravenclaw and Slytherin > Gryffindor:
		j6 = input (f' You have been chosen for 2 houses {name}, which do you prefer, [S]lytherin or [H]ufflepuff? ')
		if j6=='S':
			print('Congratulations, you are in Slytherin!')
		else:
			print('Congratulations, you are in Hufflepuff!')
	point = input(f"{name.title()}, thats the end, but would you like to know how many points you got in each house?")
	if point == 'y':
		print(f"\tGryffindor: {Gryffindor}")
		time.sleep(0.5)
		print(f"\tHufflepuff: {Hufflepuff}")
		time.sleep(0.5)
		print(f'\tRavenclaw: {Ravenclaw}')
		time.sleep(0.5)
	print(f'\tSlytherin: {Slytherin}')

def Ollivanders():
	wood = ['maple','oak','elder','spruce',]
	core = ['Dragon Heartstring','Unicorn hair','Phoenix feather']
	random.shuffle(wood)
	random.shuffle(core)
	length = ['7','8','9','10','11','12','13','14']
	random.shuffle(length)
	print('Welcome to Ollivanders Wand Shop, let me get you a wand!')
	while True:
		time.sleep(5)
		q1 = input('Does this work? y/n ')
		if q1 == 'y' or 'Y':
			break
	print(f"Good, your wand uses {wood[0]}.")
	print(f'Your wand has a {core[0]} core.')
	print(f'It is {length[0]} inches long.')
	print('This will be 5 galleons')
	while True:
		q2 = input('How much do you pay? ')
		q2 = int(q2)
		if q2 == 5:
			print('Goodbye!')
			break
		elif q2 > 5:
			print('Thanks for the tip!!')
			break
		else:
			print('not enough money!')
	print('That is the end of your shopping, time to get sorted!')
	Sorting_Hat()

def Madam_Malkins():
	print('Welcome to Madam Malkin'"'s robe shop, let me get you some robes.")
	time.sleep(15)
	status = True
	while status:
		q1 = input('Do these fit? y/n ')
		if q1 == 'y' or 'Y':
			status = False
		else:
			print('Let me get you some new ones.')
			time.sleep(5)
			status = True
	while True:
		q2 = input('The total is 5 galleons. How much do you give me? ')
		q2 = int(q2)
		if q2 > 5:
			print('Thanks for the tip!!')
			break
		elif q2 == 5:
			print('Bye, see you soon!')
			break
		else:
			print('That is not enough money.')
		
	print('Finally, you now need a wand, from Ollivanders!')
	Ollivanders()
def equitment_store():
	print('Hello, welcome to the Equitment store, let me get the stuff you need.')
	time.sleep(5)
	while True:
		q1 = input('Okay, I am done, the total is 20 galleons. How much do you give? ')
		q1 = int(q1)
		if q1 > 20:
			print('Okay, thanks for the tip, come again!')
			
			break
		elif q1 == 20:
			print('Okay, you can go! Thanks for shopping here!')
			
			break
		else:
			print('Not enough money.')
	print('Now to go to Madam Malkins, to get robes.')
	Madam_Malkins()
def Flourish_and_Blotts():
	print('Hello, welcome to Flourish and Blotts! Let me get your books. ')
	print('Okay, let me get your books real quick.')
	time.sleep(5)
	while True:
		print('Okay, I have gotten your books. The total will be 20 galleons ')
		q2 = input('How much money do you give? ')
		needed = 20	
		q2 = int(q2)
		if q2 > needed:
			print('Okay, thanks for the tip!')
			
			break
		elif q2 == needed:
			print('Okay, goodbye!')
			
			break
		else:
			print("That's not enough money, try again.")
	print('Now we will need to go to the equitment store to get your cauldron, telescope, robes, and hat.')
	equitment_store()

name = input('What is your name? ')
time.sleep(1.5)
print(f'{name.title()}, you have been accepted at Hogwarts School of Witchcraft and Wizardry! You will need the following things from Diagon Alley:')
time.sleep(1.5)
print("\t-Three sets of plain black robes.\n\n\t-One Plain Pointed Hat (Black) for day wear.\n\n\t-One Pair of Protective Gloves (dragon hide or similar).\n\n\t-One Winter Cloak (Black, silver fastenings).\n\nPlease note that all student's clothes should carry name-tags at all times.")
time.sleep(1.5)
print('Books:')
time.sleep(1.5)
print("The Standard Book of Spells by Miranda Goshawk\n\n\tA History of Magic by Bathilda Bagshot.\n\n\tMagical Theory by Adalbert Waffling\n\n\tA Beginner's Guide to Transfiguration by Emeric Switch\n\n\tOne Thousand Magical Herbs and Fungi by Phyllida Spore\n\n\tMagical Drafts and Potions by Arsenius Jigger\n\n\tFantastic Beasts and Where to Find Them by Newt Scamander\n\n\tThe Dark Forces: A Guide to Self-Protection by Quentin Trimble\nOther:\n\n\t1 wand,\n\n\t1 cauldron\n\n\t1 set of glass or crystal phials\n\n\t1 telescope\n\n\t1 set of brass scales\n\n\tYou may also bring a cat OR toad OR owl.")
time.sleep(1.5)

print(name.title(),', we will now need to get your books.')
Flourish_and_Blotts()
