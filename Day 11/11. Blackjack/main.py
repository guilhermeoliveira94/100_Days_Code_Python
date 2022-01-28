from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def start():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == "y":
        print(logo)
        deal()
    elif start == "n":
        exit()
    else:
        print("Wrong input.")

def deal():
    player_cards = []
    cpu_cards = []

    player_cards.append(cards[random.randint(0, (len(cards) - 1))])
    player_cards.append(cards[random.randint(0, (len(cards) - 1))])

    cpu_cards.append(cards[random.randint(0, (len(cards) - 1))])

    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {cpu_cards}")
    if sum(player_cards) == 21:
        print("Blackjack! You win!")
        start()
    should_continue = True
    while should_continue:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
            second_deal(player_cards, cpu_cards)
        else:
            should_continue = False
            result(player_cards, cpu_cards)

def second_deal(player_cards, cpu_cards):
    player_cards.append(cards[random.randint(0, (len(cards) - 1))])
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")

    if sum(player_cards) == 21:
        print("Blackjack! You win!")
        start()
    elif sum(player_cards) > 21:
        if 11 in player_cards:
            for i, n in enumerate(player_cards):
                if n == 11:
                    player_cards[i] = 1
            second_deal(player_cards, cpu_cards)
        print("You went over. You lose!")
        start()
    else:
        result(player_cards, cpu_cards)
        start()

def result(player_cards, cpu_cards):
    while sum(cpu_cards) < sum(player_cards) and sum(cpu_cards) < 21:
        cpu_cards.append(cards[random.randint(0, (len(cards) - 1))])

    print(f"Your cards: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {cpu_cards}, final score: {sum(cpu_cards)}")

    if sum(cpu_cards) == sum(player_cards):
        print("Its a Draw!")
        start()
    elif sum(cpu_cards) > sum(player_cards) and sum(cpu_cards) > 21:
        print("You win!")
        start()
    else:
        print("You lose!")
        start()

start()