# Split string method
names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# Forma de resolver pedida pelo desafio
aleatorio = random.randint(0,(len(names)-1))
print(f"{names[aleatorio]} is going to buy the meal today!")

# Outra forma de fazer, desta vez usando random.choice
# aleatorio = random.choice(names)
# print(f"{aleatorio} is going to buy the meal today!")