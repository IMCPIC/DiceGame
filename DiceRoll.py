import random
from random import randint

MasterDiceList = [4,6,8,10,12,20]
PlayerOneDice = [4,6,8,10,12,20]
PlayerTwoDice = [4,6,8,10,12,20]

PlayerOneWins = 0
PlayerTwoWins = 0
GamePlay = True

while (GamePlay):
	PlayerOneSelection = int(raw_input("Player One Select Dice:"))
	PlayerTwoSelection = int(raw_input("Player Two Select Dice:"))

	PlayerOneRoll = randint(1,PlayerOneSelection)
	PlayerTwoRoll = randint(1,PlayerTwoSelection)

	print ("Player One: {0}, Player Two: {1}" .format(PlayerOneRoll,PlayerTwoRoll))

	if (PlayerOneRoll > PlayerTwoRoll):
		if (PlayerOneRoll == 1):			# Player One Rolls a 1 and wins
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1):			# Player Two Rolls a 1 and wins
			GamePlay = False
			PlayerTwoWins = 2
			print("Player Two Wins Game")
		else:								
			if (PlayerTwoRoll == 2):		# Players Roll a 2
				PlayerTwoWins = PlayerTwoWins-1
			if (PlayerOneRoll == 2):
				PlayerOneWins = PlayerOneWins-1
			else:							#Total Gameplay wins+
				print ("Player One Wins Round")
				PlayerOneWins = PlayerOneWins+1
				if (PlayerOneWins == 2):
					GamePlay = False
					print ("Player One Wins Game")
	elif (PlayerOneRoll < PlayerTwoRoll):
		if (PlayerOneRoll == 1): 			# Player One Rolls a 1 and wins
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1): 			# Player Two Rolls a 1 and wins
			GamePlay = False
			PlayerTwoWins = 2
			print ("Player Two Wins Game")
		else:
			if (PlayerTwoRoll == 2):		# Players Roll a 2
				PlayerTwoWins = PlayerTwoWins-1
			if (PlayerOneRoll == 2):
				PlayerOneWins = PlayerOneWins-1
			else:							#Total Gameplay wins+
				print ("Player Two Wins Round")
				PlayerTwoWins = PlayerTwoWins+1
				if (PlayerTwoWins == 2):
					GamePlay = False
					print ("Player Two Wins Game")
	else:
		print ("Tie Game")

	print ("Player One Wins: {0}, Player Two Wins: {1}" .format(PlayerOneWins,PlayerTwoWins))



	

