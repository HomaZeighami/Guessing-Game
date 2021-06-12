# Python Random Module.
import random

# The player's guess and the number of their attempts.
guess = ""
attempts = 0

# The game chooses a random number between 1 and 20.
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20.")

# While the number of the player's attempts is less than 5, they can guess.
while attempts < 5:
    guess = input("Take a guess: ")
    guess = int(guess)
    attempts += 1

    # If the player's guess is less than the game's chosen number, they should guess a greater number.
    if guess < number:
        print("Your guess is less than my chosen number.")

    # If the player's guess is greater than the game's chosen number, they should guess a lesser number.
    if guess > number:
        print("Your guess is greater than my chosen number.")

    # If the player wins the game, the loop stops.
    if guess == number:
        break

# If the player's guess is equal to the game's chosen number, they win the game.
if guess == number:
    attempts = int(attempts)
    print("Good job! You guessed my number in", attempts, "guesses!")

# If the player is out of guesses or their guess is not equal to the game's chosen number, they lose the game.
if attempts > 5 or guess != number:
    number = int(number)
    print("You are out of guesses! The number I was thinking of was", number, ".")
