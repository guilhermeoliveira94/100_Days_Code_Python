# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data["temp"].mean())  # Print Average temperature
# print(data["temp"].max())  # Print Maximum temperature
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in Row
# print(data[data.day == "Monday"])

# # Printing the day with the highest temperature
# print(data[data.temp == data.temp.max()])
#
# # Printing the condition of Monday
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# # Printing monday's temperature to Fahrenheit
# temp_in_c = int(monday.temp)
# print(temp_in_c)
# temp_in_f = (temp_in_c * 9 / 5) + 32
# print(temp_in_f)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
