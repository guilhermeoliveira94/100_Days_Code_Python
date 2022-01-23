import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

game_images = [rock, paper, scissors]
if player_choice >= 3 or player_choice < 0:
    print("Error! Invalid number!")
else:
    print(game_images[player_choice])

    computer_choice = random.randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice])

    if (player_choice == 0 and computer_choice == 2) or (player_choice > computer_choice):
      print("You win!")
    elif (computer_choice == 0 and player_choice == 2) or (computer_choice > player_choice):
      print("You lose")
    else:
      print("It's a draw")

    # if player_choice == 0:
    #     if computer_choice == 0:
    #         print("It's a draw")
    #     elif computer_choice == 1:
    #         print("You lose")
    #     else:
    #         print ("You win!")
    # elif player_choice == 1:
    #     if computer_choice == 0:
    #         print("You win!")
    #     elif computer_choice == 1:
    #         print("It's a draw")
    #     else:
    #         print("You lose")
    # else:
    #     if computer_choice == 0:
    #         print("You lose")
    #     elif computer_choice == 1:
    #         print("You win!")
    #     else:
    #         print ("It's a draw")