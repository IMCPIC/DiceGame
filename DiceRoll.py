import random									# Randomiser reference
from random import randint

MasterDiceList = [4,6,8,10,12,20]				# Die selection pool
PlayerOneDice = [4,6,8,10,12,20]
PlayerTwoDice = [4,6,8,10,12,20]

PlayerOneWins = 0								# Game start totals
PlayerTwoWins = 0
GamePlay = True

while (GamePlay):
	
	print (PlayerOneDice)						# Selection of die and confirmation die is available
	PlayerOneSelection = int(raw_input("Player One Select Die:"))
	
	while (PlayerOneSelection not in PlayerOneDice):
		PlayerOneSelection = int(raw_input("Die Not Available. Please Select Again:"))
	
	print (PlayerTwoDice)
	PlayerTwoSelection = int(raw_input("Player Two Select Die:"))
	
	while (PlayerTwoSelection not in PlayerTwoDice):
		PlayerTwoSelection = int(raw_input("Die Not Available. Please Select Again:"))
		
	
	PlayerOneDice.remove(PlayerOneSelection)	# Removing used die from selection
	if len(PlayerOneDice) == 0:
		PlayerOneDice = MasterDiceList
	
	PlayerTwoDice.remove(PlayerTwoSelection)
	if len(PlayerTwoDice) == 0:
		PlayerTwoDice = MasterDiceList

	PlayerOneRoll = randint(1,PlayerOneSelection)	# Randomiser
	PlayerTwoRoll = randint(1,PlayerTwoSelection)

	print ("Player One: {0}, Player Two: {1}" .format(PlayerOneRoll,PlayerTwoRoll)) # Numbers rolled

	if (PlayerOneRoll > PlayerTwoRoll):
		if (PlayerOneRoll == 1):				# Player One Rolls a 1 and wins game
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1):				# Player Two Rolls a 1 and wins game
			GamePlay = False
			PlayerTwoWins = 2
			print("Player Two Wins Game")
		else:								
			if (PlayerTwoRoll == 2):			# Players Roll a 2
				PlayerTwoWins = PlayerTwoWins-1
			if (PlayerOneRoll == 2):
				PlayerOneWins = PlayerOneWins-1
			else:								# Player One wins round
				print ("Player One Wins Round")
				PlayerOneWins = PlayerOneWins+1
				if (PlayerOneWins == 2):		# Player One wins game with 2 total points
					GamePlay = False
					if (PlayerTwoWins <= -1):	# Player Two -1 trumps 2 points and wins game
						print ("Player Two Wins")
					else:
						print ("Player One Wins Game")
	elif (PlayerOneRoll < PlayerTwoRoll):
		if (PlayerOneRoll == 1): 				# Player One Rolls a 1 and wins game
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1): 				# Player Two Rolls a 1 and wins game
			GamePlay = False
			PlayerTwoWins = 2
			print ("Player Two Wins Game")
		else:
			if (PlayerTwoRoll == 2):			# Players Roll a 2
				PlayerTwoWins = PlayerTwoWins-1
			if (PlayerOneRoll == 2):
				PlayerOneWins = PlayerOneWins-1
			else:								# Player Two wins round
				print ("Player Two Wins Round")
				PlayerTwoWins = PlayerTwoWins+1
				if (PlayerTwoWins == 2):		# Player Two wins game with 2 total points
					GamePlay = False
					if (PlayerOneWins <= -1):	# Player One -1 trumps 2 points and wins game
						print ("Player One Wins")
					else:
						print ("Player Two Wins Game")
	else:										# Players roll same number and tie
		print ("Tie Game")			

	print ("Player One Wins: {0}, Player Two Wins: {1}" .format(PlayerOneWins,PlayerTwoWins)) # Total Game-play wins



	

