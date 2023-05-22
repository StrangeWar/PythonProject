# with open('weather_data.csv') as file:
#     data = file.readlines()
#     print(data)


# import csv
#
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     TEMPERATURE = []
#     for row in data:
#         TEMPERATURE.append(row[1])
#     print(TEMPERATURE)

import pandas

# data = pandas.read_csv('weather_data.csv')
# average_temp = data['temp'].mean()
# print(average_temp)
#
# max_temp = data['temp'].max()
# print(max_temp)

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print((monday.temp*(9/5))+32)
# data_dict = {'admin': ['local'], 'userA': ['local'], 'userB': ['public']}
# data = pandas.DataFrame(data_dict)
# data.to_csv('new.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count)

squirrel_dict = {'fur_color': ['gray', 'cinnamon', 'black'],
                 'squirrel_count': [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]}

data2 = pandas.DataFrame(squirrel_dict)
data2.to_csv('squirrel_count.csv')