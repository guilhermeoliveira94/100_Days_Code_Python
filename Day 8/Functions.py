# Simple function
def greet():
    print(f"Hello!")
    print("My name is Guilherme")
    print("I'm a programmer!")

greet()

# Function that allows for input
def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How do you do {name}?")
    print("I'm a programmer!")

name = input("What is your name? ")
greet_with_name(name)

# Function with more than 1 input
def greet_with_name_location(name, location):
    print(f"Hello, {name}!")
    print(f"Do you still live in {location}?")
    print("I'm a programmer!")

name = input("What is your name? ")
location = input("What is your location? ")
greet_with_name_location(name, location)