import random

min = 1
max=100
trials = 0

# define the rndom value, integer between 0 nd 10

value = random.randint(min, max)
print(value)
is_running = True
print("-------------------------------")
print("Welcome to Number Guessing Game")
print("-------------------------------")

while is_running:
    try:
        guess = int(input(f"Please enter a number between ({min} and {max}): "))
    except ValueError:
        print("Please enter a valid number")
        continue
    trials +=1

    if guess == value:
        print(f"You win! The matching number was {guess}, you made {trials} trials.")
        is_running = False
    elif guess < 0:
        print("Number can't be negative. Enter a valid number to continue:")
    elif guess < value:
        print("Number too low! Try again!")
    elif guess > value:
        print("Number too high! Try again!")

