# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
print("I love learning Python")

# Print Practice #2
print("Learning with 'TOTAL Python' is super fun!")

# Print Practice #3
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence

chair = "chair"
laptop = "laptop"
backpack = "backpack"

print(f"In my room, I have a {chair}, a {laptop}, and a {backpack}.")

# Print your name.
print("Benji")

# Print today's date.
print("October 31, 2025")

# Print the name of your favorite movie.
print("Blue Beetle")

# Print your name and age on separate lines using a single print() function.
print("Benji\n16")

# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."
name = "Benji"
age = 16
print(f"In 10 years, {name} will be {age + 10} years old.")

##############################################################################################################
########################### String Practice ##################################

blue_beetle_summary = (
    "Blue Beetle is a superhero movie about a young man named Jaime Reyes "
    "who finds an alien scarab that gives him incredible armor and powers. "
    "He must learn to control it and protect his family from dangerous enemies."
)

# print the length of the summary
print(len(blue_beetle_summary))

# upper case the entire summary
print(blue_beetle_summary.upper())

# print the summary in lowercase
print(blue_beetle_summary.lower())

# replace the word blue with red
print(blue_beetle_summary.replace("Blue", "Red"))

# string index the word beetle and print it out
print(blue_beetle_summary[5:11])  # "Beetle"

# print the last word of the summary
print(blue_beetle_summary.split()[-1])

# print the summary in reverse
print(blue_beetle_summary[::-1])

##############################################################################################################
########################## Input Practice #############################################

# Input Practice #1
learning = input("What are you learning today? ")
print(f"You are learning {learning}.")

# Input Practice #2
place = input("Where are you from? ")
print(f"You are from {place}.")

# Input Practice #3
first_name = input("What is your name? ")
surname = input("What is your surname? ")
print(f"Your full name is {first_name} {surname}.")

# Exercise:
name = input("What is your name? ")
color = input("What is your favorite color? ")
print(f"Nice to meet you, {name}! Your favorite color is {color}.") 








