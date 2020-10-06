import sys as s
import time as t
import webbrowser as w
def Common_room():
	print('Hello, welcome to the common room, where students will do activities, and complete homework.')
	w.open_new('https://i.pinimg.com/236x/e8/13/68/e813685ee6914b287fa25d5dbe4dc4c8--harry-potter-props-harry-potter-bedroom.jpg')
	w.open_new('https://i.ytimg.com/vi/5PV6MB6VcVI/maxresdefault.jpg')
	w.open_new('https://i.ytimg.com/vi/fCMybQ9cG4w/maxresdefault.jpg')
	w.open_new('https://images.ctfassets.net/usf1vwtuqyxm/7cbRXzEpTT0jpqrMwF6P2U/48c7e155e6ea5cddfd50d5dfdd7a9f42/slytherin-common-rom.jpg?fm=jpg')
	classrooms()
def classrooms():
	print('Welcome to the Charms classroom, this is where students will learn charms from Professer Flitwick.')
	w.open_new('https://vignette.wikia.nocookie.net/harrypotter/images/3/3e/Filius_teaching.jpg/revision/latest?cb=20170629202234')
	print('This is the end of this tour.')
	s.exit('Thanks for coming!')
def grounds():
	print('Welcome to the Hogwarts grounds! This is outside, as you can see! There are 2 classes located here in the grounds, Herbology and Care of Magical Creatures.\nHere is the picture:')
	w.open_new('https://images.ctfassets.net/usf1vwtuqyxm/1TD8f1pgxycgSWieMqIie4/982597def33be32c07149e79f75ef63a/HogwartsCastle_WB_F3_HogwartsCastleAndWhompingWillow_Still_080615_Land.jpg?fm=jpg')
	q1 = input('''Where do you want to go now?
		[1] Classrooms
		[2] Great Hall
		[3] Common rooms
		[4] Exit''')
	if q1 == '1':
		classrooms()
	elif q1 == '2':
		great_hall()
	elif q1 == '3':
		Common_room()
	else:
		s.exit('Goodbye, hope you had a great time!')
				
def great_hall():
	print('Hello, welcome to the Great Hall! This is where we eat.')
	t.sleep(1)
	print('Here is the image:')
	w.open_new('https://i.pinimg.com/originals/0b/ef/56/0bef56d46cd02f1ee1449de7c8873b31.jpg')	
	q1 = input('''Where do you want to go now?
		[1] Grounds
		[2] Classrooms
		[3] Exit''')
	if q1 == '1':
		grounds()
	elif q1 == '2':
		classrooms()
	elif q1 == '3':
		s.exit('Goodbye! I hope you had an amazing time! :)')
	else:
		print('Invalid character, try again.')
		s.exit(1)
	
def entrance_hall():
	print('Welcome to the entrance hall! This is where students will enter the castle.')
	t.sleep(1)
	print('Here is an image, it will be opened in a new tab.')
	w.open_new('http://images3.wikia.nocookie.net/__cb20111128012736/harrypotter/images/c/c7/Great_Hall.png')
	q1 = input('''Where do you want to go now?
		[1] Outside into the grounds
		[2] Great Hall
		[3] Exit\n\n''')
	if q1 == '1':
		grounds()
	elif q1 == '2':
		great_hall()
	elif q1 == '3':
		s.exit('Goodbye!')
	else:
		print('Invalid character')
		entrance_hall()
while True:
	name = input('Hello, welcome to Hogwarts! What is your name? ')
	if name == 'Voldemort' or name == 'Lord Voldemort' or name == 'voldemort' or name == 'lord voldemort':
		print("Goodbye, you're not doing this!!!!")
		s.exit(0)
	elif name == 'voldmort' or name == 'Voldmort':
		print('Stop impersonating Voldemort!')
	else:
		break
print('Let us now go into the Entrance Hall!')
entrance_hall()
