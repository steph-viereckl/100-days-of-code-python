import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census.csv")

# My way of doing it
fur_color_series = data["Primary Fur Color"]
fur_color_counts = fur_color_series.value_counts()
squirrel_fur_count_data_frame = pandas.DataFrame({'Fur Color': fur_color_counts.index, 'Count': fur_color_counts.values})
# Save the DataFrame to a CSV file
squirrel_fur_count_data_frame.to_csv('squirrel_count.csv', index=False)

############### Angelas way of doing it ##############

# Find the rows where the Primary Fur Color is equal to Gray and store count
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
# Create dictionary
fur_color_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count]
}

angelas_data_frame = pandas.DataFrame(fur_color_dict)
print(angelas_data_frame)

########################################################