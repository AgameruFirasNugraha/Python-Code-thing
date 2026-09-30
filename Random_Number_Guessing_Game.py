# ================================
#===SECRET NUMBER GUESSING GAME===
#=================================

# 1. Import python's random library module

import random

# 2. pick a number between 1 and 100

secret_number = random.randint(1, 100)
attempts = 0

# 3. game loop

while True:
    user_input = input("enter your guess: ")

    # to make sure there is no error for the users input, convert all the number into integer

    guess = int(user_input)
    attempts += 1  #this to make sure every attempt add 1 to the general attempts

# 4. compare the users guess to the selected random secret number

    if guess < secret_number:
        print("too LOW, Try Again")

    elif guess > secret_number:
        print("too HIGH, Try Again")

    else:
        print(f"\nBOOM!!! You Got It! the secret number was {secret_number}")
        print(f"It took you {attempts} attempts to win!")
        break
    





