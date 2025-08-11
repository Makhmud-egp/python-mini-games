# Hangman Lite - Guess the Word Game

# 1️⃣ Get secret word from Player 1 (lowercase + trimmed spaces for consistency)
secret_word = input("Enter your secret word: ").lower().strip()

# 2️⃣ Keep track of letters guessed and wrong attempts
guessed_letters = []
wrong_guess = 0
max_wrong = len(secret_word) + 2  # Player has word length + 2 chances

# 3️⃣ Main game loop: runs until player wins or runs out of guesses
while max_wrong > wrong_guess:
    
    # Display current progress (guessed letters or underscores for unknowns)
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()  # Move to new line after showing the word
    
    # 4️⃣ Get player's guess
    guess = input("Guess a letter: ").strip()

    # Validate guess: must be a single alphabetic letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter!")
        continue

    # Prevent repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Store the guess
    guessed_letters.append(guess)

    # 5️⃣ Check if guess is correct or wrong
    if guess in secret_word:
        print("Good guess!")
    else:
        wrong_guess += 1
        print("Wrong guess!")

    # 6️⃣ Win condition: all letters guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("You won!")
        print(f"Left {max_wrong - wrong_guess} wrong guesses")
        print(f"The secret word was: '{secret_word}'")
        break

    # 7️⃣ Loss condition: too many wrong guesses
    if wrong_guess >= max_wrong:
        print(f"You lose! The word was: {secret_word}")
        break
