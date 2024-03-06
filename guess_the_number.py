import os
import sys
import random 


num = random.randint(1,15)

os.system("cls")
print("\n\t### Guess The Number ###")
print("\nChoose a number between 1-15")
tries = 3
print("\nYou get 3 tries...")

while tries>0:
	try:
		value = int(input("\nEnter number (b/w 1-15): "))
	except ValueError:
		print("\nInvalid input. Please enter a valid number.")

	if value<1:
		print("\nError: value can't be smaller than 1")
		sys.exit()

	if value>15:
		print("\nError: value can't be greater than 15")
		sys.exit()

	if value==num:
		print("\nCongrats You Win!!!")
		print("\nThe number was", num)
		sys.exit()

	if value in range(num, num+3) or value in range(num-3, num):
		print("\nToo close")
	else:
		print("\nNot even close")
	tries = tries - 1
	print("\nRemaining Tries: ", tries)
	if tries==0:
		print("\nYou Loose")
		print("\nThe number was ", num)
		sys.exit()