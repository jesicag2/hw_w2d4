# HW_P5: Looping Lists - The Rhythm of Repetition

# Task 1: The for Loop DJ Set
'''
Using the provided genres list, write a for loop that prints out each genre with 
a custom message. Extend this task by adding a counter that displays the number 
of the track before the genre.
'''
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = ["This my jam!", "Eveybody put your hand up!", "Keep the beat up!", "We tunning in now"]

for i in range(len(genres)):
    genre = genres[i]
    message = messages[i]
    current_i = i + 1
    print(f"Track {current_i}: {genre} - {message}")


# Task 2: The Remix Artist with while
'''
Convert the for loop from Task 1 into a while loop. Ensure it performs the 
same function but also includes a condition to stop the loop if a certain genre 
is played for instance Hip-hop.
'''
print("\n")

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
messages = ["This my jam!", "Eveybody put your hand up!", "Keep the beat up!", "We tunning in now"]

i = 0

while i < len(genres):
    genre = genres[i]
    message = messages[i]
    current_i = i + 1
    print(f"Track {current_i}: {genre} - {message}")
    if genre == "Hip-hop":
        print("Stopping here cause we ended with a hip-hop banger")
        break
    i += 1


# Task 3: Light Show Technician Loop
'''
Using the range() function, loop through the genres list by index. For each genre, 
print out the track number and a message that the light show is ready. Modify the loop 
to skip a genre if it's not suitable for the light show, for instance Classical genre.
'''
print("\n")

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    genre = genres[i]
    current_i = i + 1
    if genre == "Rock":
        continue
    print(f"Track {current_i}: {genre} - light show is ready!")
