import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    guessed = False
    while not guessed:
            user_guess = int(input("Enter your guess: "))
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number within the range 1 to 100.")
            elif number_to_guess==user_guess:
                print("Congratulations! You guessed the correct number.")
                guessed = True
            else:
                print("Sorry, your guess is incorrect. Please try again.")
guessing_game()