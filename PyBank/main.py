import os
import csv

#"C:\Users\dakog\Desktop\Class Stuff\Mod3\python-challenge\PyBank\Resources\budget_data.csv"
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

csv_header = next(csvreader)

def data(columns):
    months = int(columns[0])
    pnl = int(columns[1])

print(len(pnl))




