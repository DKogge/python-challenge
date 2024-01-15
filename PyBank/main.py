import os
import csv
import datetime

#path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#open csv using the reader we imported in line 2
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #test to make sure the csv file loaded
    #for row in csvreader:
        #print(row)
    
    #skip the header line
    header = next(csvreader)
    
    #setting variables at start value 0
    nettotal = 0.0
    #how to loop through and count 1 column of values?  VBA allowed by column, this requires a further definition that I dont understand
    monthcount = 0.0
    #change = sum of the numbers add pos and neg together how?

    #loop time
    for row in csvreader:
        nettotal += int(row[1])
        monthcount 

    


print("Financial Analysis")
print("------------------------")
print("Total months " + str(monthcount))
print("Total: " + str(nettotal))
print("Average Change: " + str(change/monthcount))
#print("Greatest Increase in Profits: " + str(great_inc))
#print("Greatest Decrease in Profit: " + str(great_dec))