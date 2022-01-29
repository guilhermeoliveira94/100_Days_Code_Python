from art import logo, vs
from game_data import data
import random

score = 0

sorted_name_a = []
sorted_name_a.append(data[random.randint(0, len(data) - 1)])


def game():
    global score
    global sorted_name_a

    print(logo)

    sorted_name_b = []
    sorted_name_b.append(data[random.randint(0, len(data) - 1)])

    print(f"Compare A: {sorted_name_a[0]['name']}, a {sorted_name_a[0]['description']}, from {sorted_name_a[0]['country']}.")
    print(vs)
    print(f"Compare B: {sorted_name_b[0]['name']}, a {sorted_name_b[0]['description']}, from {sorted_name_b[0]['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    if guess == "a":
        guess = sorted_name_a[0]['follower_count']
        if guess > sorted_name_b[0]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}. ")
            game()

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
    elif guess == "b":
        guess = sorted_name_b[0]['follower_count']
        if guess > sorted_name_a[0]['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}. ")
            sorted_name_a = sorted_name_b
            game()

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit()
    else:
        print("Wrong input.")


game()
