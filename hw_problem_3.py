# HW_P3: Loop Condition Logic

# Task 1: Loop Condition Exploration
'''
Write a while loop with a condition that will never be true (an infinite loop). 
Inside the loop, print a statement. Then, use a break statement to exit the loop 
after 5 iterations.
'''

iteration = 0

while True: 
    print("We have to workk on saving money")
    iteration += 1
    if iteration == 5:
        break
    

# Task 2: Conditional Exit
'''
Modify the infinite loop from Task 1 to include a condition that will eventually 
be true and remove the break statement. The loop should terminate naturally once 
the condition is met.
'''
print("\n")

money = 0

while money < 100: 
    print("We have to workk on saving money")
    money += 10
