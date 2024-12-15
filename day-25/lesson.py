# Open csv
# add each line into a list called data
# import csv
#
# # Open starting letter and store in variable
# with open("weather_data.csv", mode="r") as file:
#
#     # This puts each new line into an element in an array
#     # data = file.readlines()
#     # print(data)
#
#     # Use CSV module to do this
#     data = list(csv.reader(file))
#
#     data.pop(0) # Remove the header column
#     temperatures = []
#
#     for item in data:
#         temperatures.append(int(item[1]))
#
#     print(temperatures)
#
## This is a lot of work to do just to get a column in a CSV file... that is where Pandas comes in

import pandas

# Don't need to open file as above
data = pandas.read_csv("weather_data.csv")
# data is a data frame object

data_dictionary = data.to_dict()

temps = data["temp"]
# Temps is a series object
# Series is like a column in your table

temperature_list = temps.to_list()

# Challenge - what is the average temperature

sum = 0
for temp in temperature_list:
    sum += temp

# There is also a sum() function
avg = sum / len(temperature_list)
# print(f"The average is {avg}")

# Pandas has a mean function from the Series object
# print(f"The Average Temperature is {data["temp"].mean()}")
# print(f"The Max Temperature is {data["temp"].max()}")

# Get Data in Columns
# you can access with bracket notation
# print(data["condition"])
# But you can also just write:
# print(data.condition)

# How to get data in rows of data frame (i.e. data for Monday)
# Using the column "day
# print(data[data.day == "Monday"])

# Print row in data that had the highest temp
max_temp =  data.temp.max()
# print(f"Max temp: {max_temp}")

row_with_max_temp = data[data.temp == max_temp]
# print(f"Row with max temp: {row_with_max_temp}")

monday = data[data.day == "Monday"]
# Now we can use this like a dictionary
# print(monday.condition)
print(f"Monday: {monday}")


def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

print(f"Monday temp: {monday.temp}")
monday_temp = monday.temp[0] # Get the first value in the series

# Convert Celsius to Fahrenheit
monday_fahr = celsius_to_fahrenheit(monday_temp)
print(f"Monday Temp in f {monday_fahr}")

# Create dataframe from scratch

data_dict = {
    "students": ["Harry", "Ron", "Hermoine"],
    "scores": [85, 80, 100]
}

hogwarts_data = pandas.DataFrame(data_dict)
print(hogwarts_data)

# We can also convert DataFrame to CSV
hogwarts_data.to_csv("hogwarts_grades.csv")