# TDI Data Science Task 2A
# Project: Rock, Paper, Scissors Game
# Submitted: August 27, 2024

# import necessary libraries
import numpy as np
import time

# create a function for print delay
def delay_print (message, delay=2):
    print(message)
    time.sleep(delay)

# create a list for game options
game_options = ["rock", "scissors", "paper"]

# winning conditions
winner_map = {"rock": "scissors", "scissors": "paper", "rock": "paper"}    


# define play game
def play_game():
    # main function to play the rock-paper-scissors game
    delay_print("Welcome to my TDI Data Science Task 2A task")
    delay_print("My name is Ezinne")
    time.sleep(2)

    # get player's name
    player = input("What is your name? ").strip().title()
    time.sleep(2)
    
    while True:
        # generate a random choice for computer
        computer_choice = np.random.choice(game_options)

        player_choice = input(f'Hello, {player}!\nPick an item: "rock", "paper", or "scissors": ').strip().lower()
        time.sleep(2)

        # data validation
        if player_choice not in game_options:
            player_choice = input("Invalid Option. Please pick: 'rock', 'paper', 'scissors': ")
            continue

        delay_print(f"Your opponent chose: {computer_choice} while you chose {player_choice}.")
 
        # determine the outcome of the game
        if computer_choice == player_choice:
            delay_print("It is a tie. There is no winner!")
        elif player_choice == winner_map[computer_choice]:
            delay_print(f"{player} won!")
        else:
            delay_print("Computer won!")

        # ask the players it they want to play again        
        play_again = input("Do you want to play again? 'Yes' or 'No': ").strip().title()
        if play_again != "Yes":
            time.sleep(1)
            print("Thank you for playing my game. Goodbye!")
            break

# runs the game once the script is executed
if __name__ == "__main__":
        play_game()