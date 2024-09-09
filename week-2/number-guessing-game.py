# TDI Data Science Task 2B
# Submitted on: 17th August, 2024.
# Project: Develop a Number Guessing Game
# Instructions
# - Number should be an integer between 1-20
# - 3 attempts for each round
# - Give player a hint on whether the secret number is greater or less than their guess
# - User can restart game when the 3 attempts are exhausted


# import necessary libraries: numpy to generate integers and time for sleep after promptd
import numpy as np
import time

# helper function to delay print
def delay_print(message, delay=2):
    print(message)
    time.sleep(delay)

# create a function
def guess_game():
    # create a secret number
    secret_number = np.random.randint(1,21)
    first_attempt_prompt = True
    # define maximum attempts per round
    guess_count = 3
    delay_print("Welcome to my Task 2 of the TDI Data Science Program 2024.")
    delay_print("My name is Ezinne.")
    player_name = input("What is yours? ").title()
    time.sleep(2)
    # default name if player fails to enter name
    if not player_name:
        player_name = "Player 1"
    
    while guess_count > 0:

        if first_attempt_prompt:
            delay_print(f"Welcome, {player_name}!")
            delay_print(f"I am thinking of an integer between 1 and 20.")
            first_attempt_prompt = False
            time.sleep(2)
            # data type validation
            try:
                player_guess = int(input("Guess the number: "))
                time.sleep(2)
            except ValueError:
                delay_print("Please enter a valid integer: ")
                time.sleep(2)
                continue

        else:
            try:
                player_guess = int(input("Guess a different number: "))
                time.sleep(2)
            except ValueError:
                delay_print("Please enter a valid integer: ")
                time.sleep(2)
                continue     
        
        # when player's guess is accurate 
        if player_guess == secret_number:
            delay_print(f"Good Job, {player_name}! You guessed right.")
            delay_print(f"The secret number is {secret_number}")
            break

        # when players guess is greater than the secret number
        elif player_guess > secret_number:
            delay_print("Oh, no! Your guess is greater than my secret number.")
            guess_count -= 1
            
         # when players guess is less than the secret number 
        else:
            delay_print("Nope! Your guess is less than my secret number.")
            guess_count -= 1

        if guess_count > 0:
            delay_print(f"You have {guess_count} attempts left.")
        else:
            delay_print(f"No attempt left. You failed, {player_name}!")
            delay_print(f"My secret number is {secret_number}.")
            break

# main function to control game flow and restarting
def main():
    proceed = True
    while proceed:
        guess_game()
        restart = input(f"Do you want to play again?\nYes or No: ").strip().title()
        proceed = False
        if restart == "Yes":
            guess_game()
        else:
            delay_print("Thank you for playing my game. Goodbye!")
            break

if __name__ == "__main__":
    main()