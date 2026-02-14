import random

choices = ("rock", "paper", "scissors")

print("------------------------------------")
print("Welcome to Rock-Paper-Scissors Game!")
print("------------------------------------")

is_running = True
user_count = 0
computer_count = 0



while is_running:
    computer_choice = random.choice(choices)
    
    user_choice = input("Please enter your selection (rock, paper, scissors): ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a TIE")
        user_count +=1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You WIN")
        user_count +=1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You WIN")
        user_count +=1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You WIN")
        user_count +=1
    else:
        print("Computer WIN")
        computer_count +=1
    game = input("Continue playing? y/n: ").lower()
    
    if game != "y":
        print(f"\nThank you for playing!")
        print(f"You won {user_count} time(s).")
        print(f"Computer won {computer_count} time(s).")
        is_running = False    