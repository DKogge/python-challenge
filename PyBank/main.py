import os
import csv

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
    monthcount = 0.0
    nettotal = 0.0
    change = 0.0
    greatinc = 0.0
    greatdec = 0.0

    #set dictionary names
    date = []
    pnl = []
    
    #loop time
    for row in csvreader:
        monthcount +=1
        nettotal += int(row[1]) 
        date.append(row[0]) 
        pnl.append(row[1])  
        
    #change = sum of the numbers add pos and neg together how?
    #loop through to find the greatest inc/dec using if/elif or maybe min max function?



print("Financial Analysis")
print("------------------------")
print(f"Total months: {monthcount}")
print(f"Total: {nettotal}")
#print(f"Average Change: {change}/{monthcount}")
#print(f"Greatest Increase in Profits: {greatinc}")
#print(f"Greatest Decrease in Profit: {greatdec}")

#export results to analysis folder