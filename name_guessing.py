import random

# get user's name
name = input("Who you is? ")
print("GLHF!", name)

#list of Words
words = ["diddy", "lebron", "epstein", "reza", "kanye", "elon", "trump", "biden", "putin", "musk"]

#select a random word 
word = random.choice(words)

print("\nGuess the characters")

#store guessed characters
guesses = ' '

#number of attempts
turns = 15

#main game loop
while turns > 0:

    failed = 0

    #display guessed characters and hidden letters
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1

    print()

    #check if the word has been guessed
    if failed == 0:
        print("You won!")
        print("the word is:", word)
        break

    #get user's guess
    guess = input("guess a character: "). lower()

    #validate input length
    if len(guess) != 1:
        print("Please enter a single character.")
        continue

    # check for duplicate guess
    if guess in guesses:
        print("You already guessed that character.")
        continue

    # Store the Guess
    guesses += guess

    # Handle Incorrect Guess
    if turns == 0:
        print("You lose!")
        print("the word is:", word)
        