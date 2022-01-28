############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21): # Em range é preciso considerar que o valor vai começar a contar de 0
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5) # As posições em uma lista começam a contar de 0
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994: # O ano de 1994 estava sendo pulado
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?")) # Input precisa ser Integer
# if age > 18:
#   print("You can drive at age {age}.") # Erro de indentação

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # 2 = são usados para testar igualdade, não para alocar um valor
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#
#   print(b_list)
# mutate([1,2,3,5,8,13])
