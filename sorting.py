name = input('What is your name? ')
import sys
import time
age = input(F"{name}, how old are you? ")
if age != "11":
    if age > "11":
        if age == "12" or age == "13" or age == "14" or age == "15" or age == "16" or age == "17":
            print(f"Go to your house table, {name.title()}, you are already sorted.")
            sys.exit('Already sorted.')
        elif age > "17":
            print(f"You are not attending Hogwarts any more, {name.title()}...Why are you here?")
            sys.exit('Out of school, not attending Hogwarts.')
    elif age < "11":
        print(f"You are too young, {name.title()}. Come back when you are 11 years old.")
        sys.exit['Too young.']
Gryffindor, Hufflepuff, Slytherin, Ravenclaw = 0, 0, 0, 0
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