import random

print("WELCOME")
print("PLAY ROCK PAPER SCISSORS")
print("rock=0, paper=1, scissors=2")

playerselection = input("Choose 0,1,2")
playerselection = int(playerselection) # cast as integer
computerselection = random.randint(0,2)

if computerselection == 0 and playerselection == 0:
  print("Computer throws rock")
  print("Game ends in tie")
  
