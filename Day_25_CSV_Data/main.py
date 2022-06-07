# # with open("weather_data.csv", mode="r") as data_file:
# #     data = data_file.readlines()
#
# # import csv
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# #
# # temp_list = data["temp"].to_list()
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# #
# # average_temp2 = data["temp"].mean()
# # print(average_temp2)
#
# # max_temp = data["temp"].max()
# # print(max_temp)
# #
# # # Get Data in Columns
# # print(data["condition"])
# # print(data.condition)
#
# # Get Data in Rows
# # monday = data[data.day == "Monday"]
# # print(monday)
# #
# # day_max_temp = data[data.temp == data.temp.max()]
# # print(day_max_temp)
#
# # monday = data[data.day == "Monday"]
# # monday_fahrenheit = monday.temp * (9 / 5) + 32
# # print(monday_fahrenheit)
#
# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

############################
# Primary Fur Color = color

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
