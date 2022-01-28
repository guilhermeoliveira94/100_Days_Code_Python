from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dificulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if dificulty == "hard":
    lives = 5
elif dificulty == "easy":
    lives = 10
else:
    print("Wrong input.")

rand_number = random.randint(1, 100)


def guess_number(guess):
    def victory():
        print(f"You got it! The number was {rand_number}")
        exit()

    global rand_number
    global lives

    while lives > 1 or guess == rand_number:
        if guess == rand_number:
            victory()
        elif guess > rand_number:
            lives -= 1
            print("Too hight.")
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number.")
            print("\n")
            guess = int(input("Make a new guess: "))
        else:
            lives -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {lives} attempts remaining to guess the number.")
            print("\n")
            guess = int(input("Make a new guess: "))

    print("Game over!")
    print(f"The number was {rand_number}.")
    exit()

guess = int(input("Make a guess: "))
guess_number(guess)