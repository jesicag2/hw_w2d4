# HW_P4: Python's Random Game Night

# Task 1: Random Choice Game
'''
Create a game where a player has a list of items. They have to guess which item 
in the list was selected. Use random.choice() to select the item and take the 
user's guess via input. Provide feedback on whether they guessed correctly or not.
'''

import random

straw_hat = ["Luffy", "Zoro", "Nami", "Usopp", "Sanji", "Chopper", "Robin", "Franky", "Brook"]

random_straw_hat = random.choice(straw_hat)

while True:
    fav_character = input("Guess who is the most favorite Straw Hat member? ")
    if fav_character == random_straw_hat:
        print("Good job! You guessed the favorite!")
        break
    else:
        print("Nope, try again.")
