# HW_P2: Double Scoop with Nested Loops

# Task 1: Your Mood Tracker
'''
Simulate a mood tracker that records your mood at three different times of 
the day (morning, afternoon, evening) for each day of the week. Use nested 
loops to implement this: the outer loop should iterate over the days, and the 
inner loop should iterate over the times of the day. For each time, randomly 
select a mood from a predefined list and print it.

Example Outcome: An example would be "On Tuesday afternoon you were sad" 
"On Tuesday night you were happy" "On Wednesday morning you were tired"
'''
import random

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
moods = ["happy", "sad", "energitic", "calm", "tired"]

for i in range(len(day_of_week)):
    day = day_of_week[i]
    for i in range(len(time_of_day)):
        time = time_of_day[i]
        random_mood = random.choice(moods)
        print(f"On {day} {time} you were feeling {random_mood}")
