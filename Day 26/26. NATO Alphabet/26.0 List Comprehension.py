# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# name = "Guilherme"
# letters_list = [letter for letter in name]
#
# new_range = [n * 2 for n in range(1, 5)]
# print(new_range)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# caps_long_names = [name.upper() for name in names if len(name) > 5]
# print(caps_long_names)

# # Dictionary Comprehension
# import random
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
#
# students_scores = {student: random.randint(1, 100) for student in names}
#
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

# # Dictionary Comprehension Exercise 1:
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
#
# print(result)

# # Dictionary Comprehension Exercise 2:
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# weather_f = {
#     day: value * 9/5 + 32 for (day, value) in weather_c.items()
# }
# print(weather_f)

# How to iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through a data frame
# for (key, value) in student_data_frame.items():
#     print(value)

# Loop through rows of a data frame:
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
