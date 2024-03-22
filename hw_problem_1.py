# HW_P1: The Range Riddle

# Task 1: Your Mood Today
'''
Write a program that prints off different moods for each day of the week. 
Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
Using the range() function, loop through the days of the week and for each day, 
randomly select a mood from the list and print it. Ensure that your program 
includes the use of the random module to select the mood.

Example Outcome: An example output could be "On Wednesday, you were feeling happy." 
"On Thursday you were feeling sad."
'''

import random

days_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
moods = ["happy", "sad", "energitic", "calm"]

for i in range(len(days_week)):
    day = days_week[i]
    random_mood = random.choice(moods)
    print(f"On {day}, you were feeling {random_mood}")
