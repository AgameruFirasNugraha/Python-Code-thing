#=========================
#===ROCK PAPER SCISSORS===
#=========================

# 1. import random to make sure the program to make sure a random occurrence happen

import random

# 1. make a list of available options for the program to choose randomly

choices = ["rock", "paper", "scissors"]

# 2. Score Counter

Player_score = 0
Computer_Score = 0

# 3. display the games menu

print("=== ROCK, PAPER, SCISSORS ===")
print("type 'rock', 'paper', or 'scissors' to play.")
print("type 'quit' to stop playing.\n")

#4. The heart of the game (AKA the Loop)

while True:
    user_move = input("your move: ").lower()

    # Exit Condition
    if user_move == "quit":
        print("\n====== GAME OVER ======")
        print(f"Final Score --> You: {Player_score} | Computer: {Computer_Score}")
        print("thanks For Playing")
        break

    # Matchmaking / Validation check

    if user_move not in choices:
        print(" --> [x] invalid move! pick rock, paper, or scissors.\n")
        continue #skips the rest of the loop and prompts for input again

    # Computer makes a random selection from the choices list\

    computer_move = random.choice(choices)
    print(f"Computer chose: {computer_move}")

    # 4. compare moves\
    if user_move == computer_move:
        print("--> It's a TIE!\n")

    elif (user_move == "rock" and computer_move == "scissors") or \
         (user_move == "paper" and computer_move == "rock") or \
         (user_move == "scissors" and computer_move == "paper"):
        print("--> YOU WIN this round!\n")
        Player_score += 1

    else:
        print("--> Computer Wins this round!\n")
        Computer_Score += 1
