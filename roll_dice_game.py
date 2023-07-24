Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # -*- coding: utf-8 -*-

import random

def roll_dice():
    min_value = 1
    max_value = 6
    
    while True:
        # Generate a random number between 1 and 6 (inclusive)
        dice_roll = random.randint(min_value, max_value)
        
        print(f"You rolled a {dice_roll}.")
        
        # Ask if the player wants to roll again
        roll_again = input("Do you want to roll again? (yes/no): ").lower()
        
        if roll_again != 'yes' and roll_again != 'y':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    roll_dice()
y
