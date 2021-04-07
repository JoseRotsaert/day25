# with open("./weather_data.csv", mode = "r") as data_file:
#     data =data_file.readlines()   #readlines creates a list
#     print(data)
#
# import csv
# import pandas
#
# temperature = []
# with open("./weather_data.csv", mode = "r") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
import numpy as np

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len((data[data["Primary Fur Color"] == "Gray"]))
cinnamon_squirrels_count = len((data[data["Primary Fur Color"] == "Cinnamon"]))
black_squirrels_count = len((data[data["Primary Fur Color"] == "Black"]))
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
colors_list =["Gray", "Cinnamon", "Black"]
data_dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

# temp_list = data["Primary Fur Color"].to_list()
# # print(temp_list)
# # print(temp_list.count("Gray"))
# # print(temp_list.count("Cinnamon"))
# # print(temp_list.count("Black"))
#
# for color in colors_list:
#     print(temp_list.count(color))
#     data_dictionary[color]=temp_list.count(color)

print(data_dictionary)
df = pandas.DataFrame(data_dictionary)
df.to_csv("./squirrel_count.csv")


# print(np.mean(temp_list))
# print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(((monday.temp*9)/5)+32)
