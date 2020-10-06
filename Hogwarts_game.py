import sys
import random as r
import time
fname = input('Hello, welcome to Hogwarts, what is your FIRST name? ')
lname = input('What is your last name? ')
name = fname + ' ' + lname

your_house = 'none'
day = 1

def bed(day):
	print('Time for bed!')
	print(f'It is day {day}')
	day += 1
	if library_book == 'y':
		library_book_days_left -= 1
	print('Turning off the lights.')
	time.sleep(7)
	print('The next morning...')
	print('Time to get up, sleepyhead!')
	print("Let's go to the great hall for breakfast.")
	TOD = 'morning'
	great_hall()
def library():
	choice = input(f'{fname.title()}, would you like to borrow a book? y/n ')
	if choice == 'y' or choice == 'Y':

		print(f'You are given a book.')
		print('Redirecting you to the Great hall')
		great_hall()

def Common_room(your_house):
	time_of_day = ['morning','afternoon','evening','night']
	print(f'Hello, welcome to the {your_house} Common room! What would you like to do?')
	print('[1] Go to your beds')
	print('[2] Go to the entrance hall')
	print('[3] Go to the library')
	choice = input('Choose a number. ')
	if choice == '1':
		bed(day)
	elif choice == '2':
		entrance_hall()
	elif choice == '3':
		library()
	else:
		print('Invalid character')
	Common_room()
def Sorting_Hat():
	Gryffindor = 0
	Hufflepuff  = 0
	Ravenclaw  = 0
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
		Hufflepuff += 1
		Ravenclaw+=1
	Q8 = input(f'{name.title()}, would you rather: [G]et a bad grade, [S]urrender, [B]etray someone, or [N]ot get what you want ')
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
	print(f"Gryffindor: {Gryffindor}")
	time.sleep(0.5)
	print(f"Hufflepuff: {Hufflepuff}")
	time.sleep(0.5)
	print(f'Ravenclaw: {Ravenclaw}')
	time.sleep(0.5)
	print(f'Slytherin: {Slytherin}')
	if Slytherin > Gryffindor and Slytherin > Hufflepuff and Slytherin > Ravenclaw:
		print('You are in Slytherin!')
		Slytherin_Common_Room()
	elif Gryffindor > Hufflepuff and Gryffindor > Ravenclaw and Gryffindor > Slytherin:
		print('You are in Gryffindor')
		your_house = 'Gryffindor'
	elif Ravenclaw > Hufflepuff and Ravenclaw > Gryffindor and Ravenclaw > Slytherin:
		print('You are in Ravenclaw')
		your_house = 'Ravenclaw'
	elif Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
		print('You are in Hufflepuff.')
		your_house = 'Hufflepuff'
	else:
		print('You have been chosen for multiple houses.')
		t1 = input('Based on your points, some have tied, could you tell me which? Use G for Gryffindor, H for Hufflepuff, R for Ravenclaw, and S for Slytherin. Seperate each with a comma and a space in between (Example: G, H ')
		if t1 == 'G, H' or t1 == 'H, G' or t1 == 'h, g' or t1 == 'g, h':
			t2 = ['Gryffindor','Hufflepuff']
			random.shuffle(t2)
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
		elif t1 == 'G, R' or t1 == 'R, G':
			t2 = ['Gryffindor','Ravenclaw']
			random.shuffle(t2)
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
		elif t1 == 'G, S' or t1 == 'S, G':
			t2 = ['Gryffindor','Slytherin']
			random.shuffle(t2)
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
		elif t1 == 'H, R' or t1 =='R, H':
			t2 = ['Hufflepuff','Ravenclaw']
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
		elif t1 == 'H, S' or t1 == 'S, H':
			t2 = ['Hufflepuff','Slytherin']
			random.shuffle(t2)
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
		elif t1 == 'R, S' or 'S, R':
			t2 = ['Ravenclaw','Slytherin']
			random.shuffle(t2)
			print(f'You have been chosen for {t2[0]}!')
			your_house = t2[0]
	q0 = input(f'Where do you want to go {name.title()}\n\n\t[1] Entrance Hall\n\t[2] Great hall\n\t[3] Quittich pitch\n\t[4] Common Room? ')
	if q0 == '1':
		entrance_hall()
	elif q0 == '2':
		great_hall()

	else:
		Common_room()
def great_hall(TOD, meal):
	print(f'Time for {meal}!')
	q1 = input('What do you want to eat?\n\t[1] Scrambled eggs\n\t[2] Fried eggs and bacon\n\t[3] Peanut butter and Jelly sandwich ')
	food = q1
	print('The Hogwarts house elves will get your food shortly.')
	time.sleep(3)
	print(f'Done! I have {food} here:')
	print('You eat the food.')
	go = input('What would you like to do now?\n\t[1] Common room\n\t[2] Entrance hall\n\t[3] Library')
	if go == '1':
		Common_room()
	elif go == '2':
		entrance_hall()
	elif go == '3':
		library()
def entrance_hall():
	print('You are in the entrance hall.')
	meal = ['lunch','dinner','breakfast']
	r.shuffle(meal)
	do = input(f"{fname.title()}, what would you like to do?\n\t[1] Stay here and explore\n\t[2] Go to the great hall for {meal[0]}\n\t[3] Go to your common room\n\t[4] Go to the library. ")
	if meal[0] == 'lunch':
		TOD = 'afternoon'
	elif meal[0] == 'dinner':
		TOD = 'evening'
	else:
		TOD = 'morning'
	if do == '1':
		print('You find Professer Snape.')
		print(f'He says: "What are you doing here, {lname.title()}, go to your domitory. ')
		if your_house == 'none':
			print('You need to get sorted first.')
			Sorting_Hat()
		else:
			Common_room(your_house)
	elif do == '2':
	
		if your_house == 'none':
			print('You must get sorted first.')
			Sorting_Hat()
		else:
				great_hall(TOD, meal)
	elif do == '3':
		if your_house == 'none':
			print("Let's get sorted first")
			Sorting_Hat()
		else:
			Common_room()
	elif do == '4':
		library()
entrance_hall()
