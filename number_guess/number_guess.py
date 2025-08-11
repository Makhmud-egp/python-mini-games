"""
Number Guessing Game
--------------------
A fun console-based game where the player tries to guess a randomly generated number.

Features:
- 3 difficulty levels (easy, medium, hard) that determine allowed attempts
- Number range is 1 to 20
- Input validation for non-numeric guesses
- "Close" hints if the guess is within 3 numbers of the answer
- Displays remaining attempts after each guess

Author: Makhmud-egp
Date: 08/11/2025
"""

import random  # Import random module to generate random numbers

# Difficulty levels mapped to the number of attempts
levels = {"easy": 10, "medium": 5, "hard": 3}

# Ask the player to choose a difficulty level
difficulty = input("Choose difficulty (easy/medium/hard): ").lower()

# If the choice is invalid, default to "medium"
if difficulty not in levels:
    print("Invalid choice. Defaulting to medium.")
    difficulty = "medium"

# Generate a random number between 1 and 20 (inclusive)
number = random.randint(1, 20)

# Set the number of attempts based on chosen difficulty
attempts_left = levels[difficulty]

# Main game loop: runs until the player runs out of attempts or guesses correctly
while attempts_left > 0:
    try:
        # Ask for the player's guess and convert to integer
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        # If input is not a number, ask again without losing an attempt
        print("Please enter a valid number!")
        continue

    # Decrease the attempts count after a valid guess
    attempts_left -= 1

    if guess == number:
        # guessed correctly
        print("Correct! You win 🎉")
        print(f"Attempts left: {attempts_left}")
        break
    elif number > guess:
        # The guess is too low
        if number - guess < 3:
            print("Close! But it’s a bit higher.")
        else:
            print("Too low!")
    else:
        # The guess is too high
        if guess - number < 3:
            print("Close! But it’s a bit lower.")
        else:
            print("Too high!")

    # Show remaining attempts after feedback
    print(f"Attempts left: {attempts_left}")

# If all attempts are used, reveal the correct number
if attempts_left == 0:
    print(f"Out of attempts! The number was {number}.")
