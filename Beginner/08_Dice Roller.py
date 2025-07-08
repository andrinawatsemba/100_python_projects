# Dice Roller Simulator
# This is part of my 100 Python Projects challenge.

import random

print("🎲 Welcome to Dice Roller!")

while True:
    roll = input("Roll the dice? (y/n): ").lower()
    if roll == 'y':
        print(f"You rolled: {random.randint(1, 6)}")
    elif roll == 'n':
        print("Thanks for playing! Goodbye.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
