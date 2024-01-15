import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "election_data.csv")

#open csv using the reader we imported in line 2
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #test to make sure the csv file loaded
    #for row in csvreader:
        #print(row)
    
    #skip the header line
    header = next(csvreader)

#count the number of votes
    
#list names of unique people in row[2]
    
# % each candidate won, need the total count, their count, then divide and turn into a percent
    
#list the winner - this is just getting the formatting they want
