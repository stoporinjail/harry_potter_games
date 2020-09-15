import sys
import time
import webbrowser
import os
# Assign wizard and muggle points
wizard = 0
muggle = 0

name = input("Hello! Welcome to Muggle Madness! This will determine if you are a wizard or not. What is your name? ")

if name == "Voldemort" or name == "Lord Voldemort":
    sys.exit("You're not allowed to do this quiz.")
music = input(f'{name.title()}, would you like to hear some Harry Potter music while you do this? y/n')
if music == 'y':
  
  webbrowser.open_new('https://www.youtube.com/watch?v=CvxK5pgQSIc')
  # Sometimes it does not get opened in a new tab, like when you use repl.it
  see = input(f'{name.title()}, a new tab has been opened. Do you see it? y/n')
  if see == 'y':
    print('Great!')
  else:
    print('This may be due to you using a web browser in this. If you want the link, here it is: https://www.youtube.com/watch?v=CvxK5pgQSIc Click on it.')
q1 = input(f'{name.title()}, what would you eat? \n[C]hocolate frogs \n[T]acos ')
if q1 == 'C':
    wizard += 1
else:
    muggle += 1
q2 = input(f'{name.title()}, do you know what Hogwarts is? y/n ')
if q2 == 'y':
 wizard += 1
else:
    muggle += 1
q3 = input(f'{name.title()}, Do you think that magic is real? y/n ')
if q3 == 'y':
    wizard += 1
else:
    muggle += 1
q4 = input(f'{name.title()}Do you reconize these terms: \n Muggle \n Squib \n y/n ')
if q4 == "y":
 wizard += 1
else:
    muggle += 1
q5 = input(f"{name.title()}, would you fight a death eater? y/n ")
if q5 == "y":
    wizard += 1
else:
    muggle += 1
q6 = input(f'{name.title()}, would you drink a drink called butterbeer? y/n ')
if q6 == 'y':
    wizard += 1
else:
    muggle += 1
q7 = input(f'{name.title()}, where would you go shopping? [D]iagon Alley, [K]nockturn Alley, [H]ogsmede or [O]ther? ')
if q7 == 'D' or q7 == 'K' or q7 == 'H':
    wizard += 1
else:
    muggle += 1
q8 = input(f"{name.title()}, has anything unexpected happened that you couldn't explain? y/n ")
if q8 == "y":
    wizard  += 1
else:
    muggle += 1
if muggle > wizard:
 print("You have been tested, and found to be a Muggle!")
 print("Since you are a muggle, you can not continue.")
 sys.exit(0)
elif muggle == wizard:
 print("The score is equal, and you are a squib!")
 print("You are not a wizard, but you have wizard parents. You do not belong in Hogwarts, so you cannot do the sorting.")
 sys.exit(0)
elif wizard > muggle:
 print("We checked and it seems you are a wizard")
 print("Now it is time for the sorting.")
 os.system('python sorting.py')