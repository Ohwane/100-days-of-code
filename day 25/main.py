# with open("weather_data.csv", mode="r") as data:
#    weather_d = data.readlines()
#
# print(weather_d)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas as pd

data = pd.read_csv("nyc_squirrels.csv")

fur = {"fur_colour": ["red", "black", "gray"],
       "number": []}
cinnamon = len(data[data.primary_fur_color == "Cinnamon"])
black = len(data[data.primary_fur_color == "Black"])
gray = len(data[data.primary_fur_color == "Gray"])

print((data[data.primary_fur_color == "Cinnamon"].primary_fur_color))

fur["number"].append(cinnamon)
fur["number"].append(black)
fur["number"].append(gray)
print(fur)
fur_data = pd.DataFrame(fur)

# fur_data.to_csv("fur_data.csv")

# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
#
# print(data_list)
#
# total_temp = 0
# for temp in data_list:
#     total_temp += temp
#
# avg_temp = total_temp/len(data_list)
#
# print(avg_temp)
#
# print(sum(data_list)/len(data_list))
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data.temp.max())
#
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"].temp * 9/5 + 32
#
# print(monday)
#
# data_dict = {"students": ["ohwane", "sokka", "katara"],
#              "score": [70, 55, 65]}
#
# new_data = pd.DataFrame(data_dict)
#
# new_data.to_csv("new_data.csv")
