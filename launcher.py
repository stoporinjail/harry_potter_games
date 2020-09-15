import time
import os
print('Muggle madness will be beginning soon')

try:
  # Make sure the whole repo is cloned
  os.system('python muggle_madness.py')
except:
  # If not all
  print('Please clone the whole repo from github.')
  os.system('git clone https://github.com/stoporinjail/harry_potter_games')
  

