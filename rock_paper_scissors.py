import random
cpu = random.randint(1,3)

user = input ("Enter rock, paper, or scissors ")

if user == "rock":
	if cpu == 1: # cpu chose rock 
		print("Tied")
	elif cpu == 2: #cpu chose paper
		print("You Lost")
	else: # cpu chose scissors
		print("You Win!")

if user == "paper":
	if cpu == 1: # cpu chose rock 
		print("You Win!")
	elif cpu == 2: #cpu chose paper
		print("Tied")
	else: # cpu chose scissors
		print("You Lost")

if user == "scissors":
	if cpu == 1: # cpu chose rock 
		print("You Lost")
	elif cpu == 2: #cpu chose paper
		print("You Win!")
	else: # cpu chose scissors
		print("Tied")