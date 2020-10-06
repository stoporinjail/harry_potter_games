import urllib.request
import json
import random
print('Hi, welcome to the Harry Potter characters API dictionary!')
url = 'http://hp-api.herokuapp.com/api/characters'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
correct = 0
wrong = 0
q = input('How many questions do you want? ')
q = int(q)

for i in range(q):
	number = random.randint(0, 20)
	choice = input(f"Do you know what {result[number]['name']}'s eye color is?  ")
	if choice == result[number]["eyeColour"]:
		print('You are correct!')
		correct += 1
	else:
		print("Sorry, that's the wrong answer :(")
		wrong += 1
print(f'You got {correct} out of 10!')
