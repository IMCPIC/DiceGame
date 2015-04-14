import random
from random import randint

MasterDiceList = [4,6,8,10,12,20]
PlayerOneDice = [4,6,8,10,12,20]
PlayerTwoDice = [4,6,8,10,12,20]

PlayerOneSelection = int(raw_input("Player One Select Dice:"))
PlayerTwoSelection = int(raw_input("Player Two Select Dice:"))

PlayerOneRoll = randint(1,PlayerOneSelection)
PlayerTwoRoll = randint(1,PlayerTwoSelection)

PlayerOneWins = 0
PlayerTwoWins = 0
GamePlay = True

print ("Player One: {0}, Player Two: {1}" .format(PlayerOneRoll,PlayerTwoRoll))

if (PlayerOneRoll > PlayerTwoRoll):
    print ("Player One Wins")
	PlayerOneWins = PlayerOneWins+1
	
elif (PlayerOneRoll < PlayerTwoRoll):
	print ("Player Two Wins")
	PlayerTwoWins = PlayerTwoWins+1
else:
	print ("Tie Game")


	

