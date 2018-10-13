import random

print("WELCOME")
print("PLAY ROCK PAPER SCISSORS")
numberofgames = raw_input("How many games do you want to play? (MAX 5)")
numberofgames = int(numberofgames)
currentgame = 1
computerwins = 0
playerwins = 0
tiegames = 0
while currentgame <= numberofgames:
  print("rock=0, paper=1, scissors=2")
  playerselection = input("Choose 0,1,2")
  playerselection = int(playerselection) # cast as integer
  computerselection = random.randint(0,2)
  if computerselection == 0 and playerselection == 0:
    print("Computer throws rock")
    print("Game ends in tie")
    tiegames = tiegames + 1
  elif computerselection == 0 and playerselection == 1:
    print("Computer throws rock")
    print("YOU WIN")
    playerwins = playerwins + 1
  elif computerselection == 1 and playerselection == 0:
    print("Computer throws paper")
    print("I WIN")
    computerwins = computerwins + 1
  elif computerselection == 1 and playerselection == 2:
    print("Computer throws paper")
    print("YOU WIN")
    playerwins = playerwins + 1
  elif computerselection == 2 and playerselection == 1:
    print("Computer throws scissors")
    print("I WIN")
    computerwins = computerwins + 1
  elif computerselection == 2 and playerselection == 0:
    print("Computer throws scissors")
    print("YOU WIN")
    playerwins = playerwins + 1
  elif computerselection == 0 and playerselection == 2:
    print("Computer throws scissors")
    print("I WIN")
    computerwins = computerwins + 1
  elif computerselection == 2 and playerselection == 2:
    print("Computer throws scissors")
    print("Game ends in tie")
    tiegames = tiegames + 1
  elif computerselection == 1 and playerselection == 1:
    print("Computer throws paper")
    print("Game ends in tie")
    tiegames = tiegames + 1
  # Before currentgame is incremented, check to see
  # if the current game is equal to the number of games.
  # if the current game is equal to the number of games,
  # then print out the results.
  
  currentgame = currentgame + 1
  
