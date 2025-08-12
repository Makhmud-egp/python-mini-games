import random

# available choices
choice_list = ["rock", "paper", "scissors"]

# score counters
user_point = 0
computer_point = 0

# best of 3 - first to 3 points wins
while user_point < 3 and computer_point < 3:

    # get user choice
    u_choice = input("Enter your choice(rock, paper, scissors): ").lower().strip()

    # check input
    if u_choice not in choice_list:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    
    # computer choice
    c_choice = random.choice(choice_list)
    print(f"{u_choice} vs {c_choice}")


    # determine winner for this round
    if u_choice == c_choice:
        print("It`s a draw!")
    elif (
        (u_choice == "rock" and c_choice == "scissors") or
        (u_choice == "paper" and c_choice == "rock") or
        (u_choice == "scissor" and c_choice == "paper")
    ):
        print("You win this round!")
        user_point += 1
    else:
        print("Computer wins this round!")
        computer_point += 1
    
    # show scores
    print(f"Score (Computer vs You): {computer_point} : {user_point}")
    print("-" * 30)

# final result
if user_point == 3:
    print("🎉 Congratulations! You won the game!")
else:
    print("💻 Computer wins the game!")
print("Thank you for playing")
    
