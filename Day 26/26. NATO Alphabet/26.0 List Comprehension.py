numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Guilherme"
letters_list = [letter for letter in name]

new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
caps_long_names = [name.upper() for name in names if len(name) > 5]
print(caps_long_names)
