import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#open csv using the reader we imported in line 2
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header line
    header = next(csvreader)
    
    #setting variables at start value 0
    monthcount = 0
    nettotal = 0.0
    change = 0.0
    greatinc = [0, ""]
    greatdec = [10000000, ""]

    #set list names
    date = []
    pnl = []
    
    #read in first info
    firstrow = next(csvreader)
    monthcount +=1
    nettotal += int(firstrow[1])
    previous = int(firstrow[1])

    #loop time
    for row in csvreader:
        monthcount +=1 
        nettotal += int(row[1]) 
        change = int(row[1])-previous
        previous = int(row[1])
        date.append(row[0]) 
        pnl.append(change)  

        if change > greatinc[0]:
            greatinc[0]=change
            greatinc[1]=row[0]

        if change < greatdec[0]:
            greatdec[0]=change
            greatdec[1]=row[0]
        
avemonthlychange = sum(pnl)/len(pnl)

# print info
result = f"""
Financial Analysis
----------------------------
Total Months: {monthcount}
Total: ${nettotal}
Average Change: ${avemonthlychange:.2f}
Greatest Increase in Profits: {greatinc[1]} (${greatinc[0]})
Greatest Decrease in Profits: {greatdec[1]} (${greatdec[0]})
"""

print(result)

#export results to analysis folder
output = os.path.join("analysis", "budget_analysis.txt")
with open(output,'w')as file:
    file.write(result)