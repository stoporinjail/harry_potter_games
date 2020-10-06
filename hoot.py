import random
import sys
def newts():
	points = 0
	name =input("What is your name?")
	examiner = ['Professer Tofty', 'Professer Snape','Professer McGonagall', 'Professer Umbridge','Profefsser Dumbledore']
	random.shuffle(examiner)
	print("Hi, I am Professer Marchbanks, I am the overseer for the OWLs.")
	print(f'{examiner[1]} will see you now.')
	print(f'Hi, {name.title()}, I am {examiner[1]}, I will be your examiner today.')
	print(f'Nice to meet you, {name.title()}!')
	print('Let''s begin this NEWT!')
	wrong = ['Makes them fall asleep during class','Makes them weird and their ears fall off','Makes them turn blue','Makes them sprout tentacles','Makes them barf slugs','Makes them lose their legs','Makes you burst into fire like a phoenix','Makes your head fall off','Gives you really amazing hair','Makes you into a teleporting acromantula','You get spattergoit','You get a horcrux','Your head implodes','You fall into a giant bucket of cauldron slime','Makes your arms glued to your sides','Makes you grow wings','Makes you grow another head','Makes you always answer the wrong answer','Makes you Dmub','Makes you into a dinosaur','Makes you into a dementor','Makes you mute for five minutes','Makes you into a House Elf']
	print(f'{name.title()}, first question: What does "Impervius" do?')
	random.shuffle(wrong)
	print(f'[1] {wrong[1]}')
	print(f'[2] {wrong[2]}')
	print(f'[3] It makes the object/person casted on repel water.')
	print(f'[4] {wrong[3]}')
	NEWT_q1 = input("Choose a number")
	if NEWT_q1 == '3':
		points+=2
	else:
		points-=1
	print(f'{name.title()}, here is the 2nd question')
	print("What does Felix Felisous do?")
	random.shuffle(wrong)
	print(f'[1] {wrong[1]}')
	print(f'[2] {wrong[2]}')
	print(f'[3] {wrong[3]}')
	print('[4] You get lucky')
	NEWT_q2 = input('Choose a number.')
	if NEWT_q2 == '4':
		points += 2
	else:
		points -= 1
	random.shuffle(wrong)
	print(f'{name.title()}, here is the 4th question.')
	print(f'What does Crucio do?')
	print(f'[1] It tortures the person')
	print(f'[2] {wrong[2]}')
	print(f'[3] {wrong[3]}')
	NEWT_q3 = input(f'[4] {wrong[4]}\nChoose a number. ')
	if NEWT_q3 == '1':
		points  += 2
	else:
		points -= 1 
	random.shuffle(wrong)
	print(name.title(),'here is the 4th question.\nWhat does Impedimenta do?')
	print(f'[1] {wrong[1]}')
	print(f'[2] {wrong[2]}')
	print(f'[3] {wrong[3]}')
	print(f'[4] It makes the thing/person casted on slower.')
	NEWT_q4 = input("Choose a number.")
	if NEWT_q4 == '4':
		points += 2
	else:
		points -= 1
	random.shuffle(wrong)
	print(f'{name.title()}, here is the 5th question:\nWhat does Relashio do?')
	print(f'[1] {wrong[1]}')
	print(f'[2] {wrong[2]}')
	print(f'[3] It makes the grip on something looser.')
	print(f'[4] {wrong[3]}')
	NEWT_q5 = input('Choose a number. ')
	if NEWT_q5 == '3':
		points += 2
	else:
		points -= 1
	print("That's the end, you should get your results in 1 month.")
	print('*1 month later*')
	#print(f'You got {points} point(s).') (optional)
	if points == 12 or points == 11:
		print('You got an Outstanding!')
	elif points == 10 or points == 9:
		print("You got Exceeds Expectations!")
	elif points == 8 or points == 7:
		print("You got an acceptable!")
	elif points == 6 or points == 5 or points == 4:
		print("You got a Poor!")
	elif points == 4 or points == 3 or points == 2:
		print("You got a dreadful!")
	else:
		print("You got a TROLL!")
def owl():
	point = 0 
	wrong = ['Makes them fall asleep during class','Makes them weird and their ears fall off','Makes them turn blue','Makes them sprout tentacles','Makes them barf slugs','Makes them lose their legs','Makes you burst into fire like a phoenix','Makes your head fall off','Gives you really amazing hair','Makes you into a teleporting acromantula','You get spattergoit','You get a horcrux','Your head implodes','You fall into a giant bucket of cauldron slime','Makes your arms glued to your sides','Makes you grow wings','Makes you grow another head','Makes you always answer the wrong answer','Makes you Dmub','Makes you into a dinosaur','Makes you into a dementor','Makes you mute for five minutes','Makes you into a House Elf']
	print(f"Hi, welcome to the OWL!")
	name = input("What is your name")
	examiner = ['Professer Tofty', 'Professer Snape','Professer McGonagall', 'Professer Umbridge','Profefsser Dumbledore']
	random.shuffle(wrong)
	random.shuffle(examiner)
	print(f'Hi, {name.title()}, I am {examiner[1]}, I am your examiner')
	print(f"{name}, here is your first question:")
	print("What do dementors do?")
	print(f'[1] {wrong[1]}')
	print(f'[2] {wrong[2]}')
	print(f'[3] {wrong[3]}')
	print(f'[4] Sucks all the hapiness out of you')
	OWL_q1 = input("Choose a number ")
	if OWL_q1 == '4':
		point += 2
	else:
		point -= 1
	random.shuffle(wrong)
	print(f'{name}, here is the second question')
	print(f'What does the "Wingardium Leviosa" spell do?')
	print(f'[1] Makes things float')
	print(f'[2] {wrong[3]}')
	print(f'[3] {wrong[7]}')
	print(f'[4] {wrong[-10]}')
	OWL_q2 = input("Choose a number.")
	if OWL_q2 == '4':
		point += 2
	elif OWL_q2 != '4':
		point -= 1
	random.shuffle(wrong)
	print(f'{name.title()}, here is the 3rd question.')
	print('What does "Reducto" do?')
	print(f'[1] {wrong[5]} \n [2]{wrong[3]} \n [3] Makes things explode \n [4] {wrong[10]}')
	OWL_q3 = input("Choose a number")
	if OWL_q3 == '3':
		point += 2
	else:
		point -= 1
	OWL_q4 = input(f'{name.title()}, here is the 4th question. \n What does veriteserum do? \n [1] {wrong[1]} \n [2] {wrong[2]}  \n [3] Makes you tell the truth. \n [4] {wrong[3]}  \n Choose a number.')
	if OWL_q4 == '3':
		point += 2
	else:
		point -= 1
	print(f'{name.title()}, here is the 5th question.')
	print(f'What does the polyjuice potion do?')
	print(f'[1] {wrong[3]}')
	print(f'[2]{wrong[2]}')
	print(f'[3] {wrong[1]}')
	print('[4] Makes you turn into someone else.')
	OWL_q5 = input('Choose a number.')
	if OWL_q5 == '4':
		point += 2
	else:
		point -= 1
	print("That's the end, you should get your results in 1 month.")
	print('*1 month later*')
	print(f'You got {point} point(s).') 
	if point == 12 or point == 11:
		print('You got an Outstanding!')
	elif point == 10 or point == 9:
		print("You got Exceeds Expectations!")
	elif point == 8 or point == 7:
		print("You got an acceptable!")
	elif point == 6 or point == 5 or point == 4:
		print("You got a Poor!")
	elif point == 4 or point == 3 or point == 2:
		print("You got a dreadful!")
	else:
		print("You got a TROLL!")
exam = input(f'What year are you in in Hogwarts (write number only)')
if exam == '5':
  owl()
elif exam == '7':
  print("Hope you're ready for your NEWTS!")
  newts()
else:
  sys.exit("I'm sorry, you must be either 5th year or 7th year to take the online exams")

