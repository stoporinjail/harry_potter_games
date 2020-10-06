import urllib.request
import time
import os
try:
	import json
	import urllib.request
except ImportError:
	device = input('Are you using [W]indows [M]ac, or [L]inux? ')
	if device == 'W' or device == 'w':
		os.system('pip install requests --user')
	else:
		os.system('pip install request --user')
import random
print('Hi, welcome to the Harry Potter characters patronus test, using the API!')

url = 'http://hp-api.herokuapp.com/api/characters'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
correct = 0
wrong = 0
q = input('How many questions do you want? (DO NOT PUT A HIGH NUMBER UNLESS YOU WANT YOUR COMPUTER CRASHED!) Say random for random. ')
if q == 'random' or q == 'Random':
	q = random.randint(4, 15)
	print(f'You wil have {q} questions!')
else:	
	q = int(q)
question = 0
for i in range(q):
	question += 1
	print("This is question", question)
	number = random.randint(0, 20)
	choice = input(f"Do you know what {result[number]['name']}'s patronus is? (if you think it's not listed, please do not type in anything, and click enter) ")
	if choice == result[number]["patronus"] or choice == result[number]["patronus"].title() or choice == result[number]["patronus"].upper():
		
		print('You are correct!')
		correct += 1
	else:
		print("Sorry, that's the wrong answer :(")
		wrong += 1
print(f'You got {correct} out of {q}!')
if correct > wrong:
	print('You really know the patronuses!')
elif wrong > correct:
	print("You don't know many patronuses :(")
