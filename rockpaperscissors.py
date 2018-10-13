import random

print("WELCOME")
print("PLAY ROCK PAPER SCISSORS")
numberofgames = raw_input("How many games do you want to play? (MAX 5)")
numberofgames = int(numberofgames)
currentgame = 1
while currentgame <= numberofgames:
  print("rock=0, paper=1, scissors=2")
  playerselection = input("Choose 0,1,2")
  playerselection = int(playerselection) # cast as integer
  computerselection = random.randint(0,2)
  if computerselection == 0 and playerselection == 0:
    print("Computer throws rock")
    print("Game ends in tie")
  elif computerselection == 0 and playerselection == 1:
    print("Computer throws rock")
    print("YOU WIN")
  elif computerselection == 1 and playerselection == 0:
    print("Computer throws paper")
    print("I WIN")
  elif computerselection == 1 and playerselection == 2:
    print("Computer throws paper")
    print("YOU WIN")
  elif computerselection == 2 and playerselection == 1:
    print("Computer throws scissors")
    print("I WIN")
  elif computerselection == 2 and playerselection == 0:
    print("Computer throws scissors")
    print("YOU WIN")
  elif computerselection == 0 and playerselection == 2:
    print("Computer throws scissors")
    print("I WIN")
  elif computerselection == 2 and playerselection == 2:
    print("Computer throws scissors")
    print("Game ends in tie")
  elif computerselection == 1 and playerselection == 1:
    print("Computer throws paper")
    print("Game ends in tie")
  currentgame = currentgame + 1
