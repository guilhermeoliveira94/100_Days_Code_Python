# Tip Calculator
# Instructions
#
# If the bill was $150.00, split between 5 people, with 12% tip.
#
# Each person should pay (150.00 / 5) * 1.12 = 33.6
#
# Format the result to 2 decimal places = 33.60
#
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
#
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# Example Input
#
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7
#
# Example Output
#
# Each person should pay: $19.93
#
# Hint
#
#     How to round a number to 2 decimal places in Python
#     How to limit a float to two decimal places in Python
#
# Solution
#
# https://replit.com/@appbrewery/tip-calculator-end

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? "))
number_people = int(input("How many people to split the bill? "))
result = "{:.2f}".format(bill / number_people * (1 + tip_percentage /100), 2) #Formatação para exibir zero para completar duas casas decimais
print(f"Each person should pay: ${result}")