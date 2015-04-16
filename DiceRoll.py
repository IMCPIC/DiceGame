import random									# Randomiser reference
from random import randint

MasterDiceList = [4,6,8,10,12,20]				# Die selection pool
PlayerOneDice = [4,6,8,10,12,20]				# Player Ones availible dice
PlayerTwoDice = [4,6,8,10,12,20]				# Player two availible dice

PlayerOneWins = 0								# Player Ones wins
PlayerTwoWins = 0								# Player Twos wins
GamePlay = True									# Loop controller

while (GamePlay):								# Game play control loop
	
	print (PlayerOneDice)						# Selection of die and confirmation die is available
	PlayerOneSelection = int(raw_input("Player One Select Die:")) #Player One dice selection
	
	while (PlayerOneSelection not in PlayerOneDice):				#Invalid dice loop
		PlayerOneSelection = int(raw_input("Die Not Available. Please Select Again:"))
	
	print (PlayerTwoDice)
	PlayerTwoSelection = int(raw_input("Player Two Select Die:"))	#Player two dice selection
	
	while (PlayerTwoSelection not in PlayerTwoDice):				#Invalid dice loop
		PlayerTwoSelection = int(raw_input("Die Not Available. Please Select Again:"))
		
	
	PlayerOneDice.remove(PlayerOneSelection)	# Removing used die from selection
	if len(PlayerOneDice) == 0:					# Re-adding dice to the players list
		PlayerOneDice = MasterDiceList
	
	PlayerTwoDice.remove(PlayerTwoSelection)
	if len(PlayerTwoDice) == 0:					# Re-adding dice to the players list
		PlayerTwoDice = MasterDiceList

	PlayerOneRoll = randint(1,PlayerOneSelection)	# Player ones random roll
	PlayerTwoRoll = randint(1,PlayerTwoSelection)	# Player twos random roll

	print ("Player One: {0}, Player Two: {1}" .format(PlayerOneRoll,PlayerTwoRoll)) # Numbers rolled

	if (PlayerOneRoll > PlayerTwoRoll):			# Check if player 1 dice is greater
		if (PlayerOneRoll == 1):				# Player one auto wins
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1):				# Player two auto wins
			GamePlay = False
			PlayerTwoWins = 2
			print("Player Two Wins Game")
		else:								
			if (PlayerTwoRoll == 2):			# Player 2 loses a win
				PlayerTwoWins = PlayerTwoWins-1
			if (PlayerOneRoll == 2):			# Player 1 loses a win
				PlayerOneWins = PlayerOneWins-1
			else:								# Player One wins round
				print ("Player One Wins Round")
				PlayerOneWins = PlayerOneWins+1
				if (PlayerOneWins == 2):		# Check if player 1 has won the game
					GamePlay = False
					if (PlayerTwoWins <= -1):	# Check if player 2 has -1 wins to auto win
						print ("Player Two Wins")
					else:
						print ("Player One Wins Game")
	elif (PlayerOneRoll < PlayerTwoRoll):		# Player 2 roll is greater
		if (PlayerOneRoll == 1): 				# Player 1 auto win
			GamePlay = False
			PlayerOneWins = 2
			print ("Player One Wins Game")
		elif (PlayerTwoRoll == 1): 				# Player 2 auto win
			GamePlay = False
			PlayerTwoWins = 2
			print ("Player Two Wins Game")
		else:									
			if (PlayerOneRoll == 2):			# Player 1 loses a win
				PlayerOneWins = PlayerOneWins-1
			if (PlayerTwoRoll == 2):			# Player 2 loses a win
				PlayerTwoWins = PlayerTwoWins-1
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



	

