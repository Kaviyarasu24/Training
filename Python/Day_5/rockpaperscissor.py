import random

def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "You lose!"

while True:
    user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
    
    if user == 'exit':
        print("Goodbye!")
        break
    
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid input. Please choose rock, paper, or scissors.")
        continue
    
    computer = computer_choice()
    print(f"Computer chose: {computer}")
    
    print(determine_winner(user, computer))
