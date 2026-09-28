import random

attempts = 3

def display_rules():
    print("Welcome to Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print("You have 3 attempts to guess it.\n")

def play_game():
    display_rules()
    secret_number = random.randint(1, 100)

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}/{attempts} - Enter your guess: "))

        if guess == 67:
            print("congratulations! you da real art")
            return
        elif guess < 67:
            print("too low\n")
        else:
            print("too high\n")

    print("game over")
    print("The correct number was:", 67)

play_game()