#Name: Jeffrey Shen
#Student ID: 10153021
#CPSC 231 T04
#This program is a simple game that requires the user to set the dial in the pantry to red and the lever in the kitchen to backwards.
#After the dial is red and the lever is backwards, the user can now enter the locked door in the entrance room.
#A limitation to this game is that it does not continue after entering the locked door. The user is unable to go back into the entrance room or continue into further rooms
entranceroom = True
leverforward = True
dialgreen = True
dialblue = True
finalcheck = True
#This is the main loop that continuously until the user sets the dial the red, pulls the lever backwards and enters the locked room
while leverforward or dialgreen or dialblue or finalcheck:
# The entrance room presents the user with three choices.
# The user can either choose to go the kitchen, go to the pantry, or try to open the locked door.
# The user will be unable to open the locked room unless the dial is set to red and lever is pulled backwards.
# When the user tries to open the locked door after setting the dial in the pantry to red, and pulling the lever backwards in the kitchen, the game will end.
	if entranceroom:
		print("\nRoom: Entrance")
		print("----------------")
		print("You are in the entrance room and the door you used to enter is permanently closed.\n")
		print("You have the following options:")
		inputNeeded = True
		while inputNeeded:
			print("1: Go to kitchen")
			print("2: Go to pantry")
			print("3: Try to open the locked door")
			choice = input("Your choice: ")
			if choice in ("1", "2"):
				inputNeeded = False
			elif choice == "3":
				if leverforward or dialgreen or dialgreen:
					print("\nThe room is locked.")
				else:
					inputNeeded = False
					print("The door is unlocked, congratulations!")
			else:
				print("Wrong choice, try again.")
		if choice == "1":
			entranceroom = False
			currentRoom = 1
		elif choice == "2":
			entranceroom = False
			currentRoom = 2
		elif choice == "3":
			finalcheck = False
#The Kitchen presents three options for the user.
#The user can either push the lever forward, pull the lever backwards, or return to the entrance room.
	elif currentRoom == 1:
		print("\nRoom: Kitchen")
		print("----------------")
		print("You are in now in the Kitchen.")
		print("In front of you is a lever which can be pushed into the forward position or pulled into the backward postion.")
		print("Behind you is entrance room.")
		Kitchen = True
		while Kitchen:
			if leverforward:
				print( "\nThe lever is currently set to forward.")
			else:
				print( "\nThe lever is currently set to backward.")
			print("You have the following options:")
			inputNeeded = True
			while inputNeeded:
				print(" 1: Push the lever forward.")
				print(" 2: Pull the lever backward.")
				print(" 3: Go back to the entrance room.")
				choice = input("Your choice: ")
				if choice in ("1", "2", "3"):
					inputNeeded = False
				else:
					print("Please choose again.")
			if choice == "1":
				leverforward = True
			elif choice == "2":
				leverforward = False
			elif choice == "3":
				Kitchen = False
				entranceroom = True
# The pantry presents the user with four options.
# The user can choose to turn the dial to blue, green, red or return to the entrance room.
	elif currentRoom == 2:
		print("\nRoom: Pantry")
		print("----------------")
		print("You're in the pantry that contains the usual foodstuffs.")
		print("In front of you is a dial with 3 settings: blue, red and green. Behind you is the entrance room.")
		Pantry = True
		while Pantry:
			if dialblue:
				print("\nThe dial is turned to blue.")
			elif dialgreen:
				print("\nThe dial is turned to green.")
			else:
				print("\nThe dial is turned to red.")
				dialgreen = False
				dialblue = False
			inputNeeded = True
			while inputNeeded:
				print(" 1: Turn the dial to blue.")
				print(" 2: Turn the dial to green.")
				print(" 3: Turn the dial to red.")
				print(" 4: Return to the entrance room.")
				choice = input("Your choice: ")
				if choice in ("1", "2", "3", "4"):
					inputNeeded = False
				else:
					print("Please choose again.")
			if choice == "1":
				dialblue = True
			elif choice == "2":
				dialblue = False
				dialgreen = True
			elif choice == "3":
				dialblue = False
				dialgreen = False
			elif choice == "4":
				Pantry = False
				entranceroom = True
