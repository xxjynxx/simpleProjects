import random

print("\n--- Dice Rolling Simulator ---")

dice_sides = ['\n-----\n|   |\n| o |\n|   |\n-----',
			  '\n-----\n|o  |\n|   |\n|  o|\n-----',
			  '\n-----\n|o  |\n| o |\n|  o|\n-----',
			  '\n-----\n|o o|\n|   |\n|o o|\n-----',
			  '\n-----\n|o o|\n| o |\n|o o|\n-----',
			  '\n-----\n|o o|\n|o o|\n|o o|\n-----'
			  ]

choice = random.choice(dice_sides)

print(choice)