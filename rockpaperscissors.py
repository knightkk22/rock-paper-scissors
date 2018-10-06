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
if computerselection == 0 and playerselection == 1:
  print("Computer throws rock")
  print("YOU WIN")
if computerselection == 1 and playerselection == 0:
  print("Computer throws paper")
  print("I WIN")
if computerselection == 1 and playerselection == 2:
  print("Computer throws paper")
  print("YOU WIN")
if computerselection == 2 and playerselection == 1:
  print("Computer throws scissors")
  print("I WIN")
if computerselection == 2 and playerselection == 0:
  print("Computer throws scissors")
  print("YOU WIN")
if computerselection == 0 and playerselection == 2:
  print("Computer throws scissors")
  print("I WIN")
if computerselection == 2 and playerselection == 2:
  print("Computer throws scissors")
  print("Game ends in tie")
if computerselection == 1 and playerselection == 1:
  print("Computer throws paper")
  print("Game ends in tie")
