import pandas as pd
import csv

data_file = open("weather_data.csv") 
temperatures = []

data = csv.reader(data_file)
next(data)


for row in data:
    temperatures.append(row[1])

print(temperatures)