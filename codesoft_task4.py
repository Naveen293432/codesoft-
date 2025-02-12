import random

def play_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors, or 'q' to quit): ").lower()
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue  
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")



# Start the game
play_rock_paper_scissors()
