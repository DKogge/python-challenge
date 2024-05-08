import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "election_data.csv")

#open csv using the reader we imported in line 2
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header line
    header = next(csvreader)

    #set variables and lists ect
    votes = 0
    names = []
    candidate_votes = {}
    winner = ""
    winner_count = 0

    for row in csvreader:
        #count the total number of votes
        votes +=1  

        #pull in the name, see if it is in the list, if not add it and add to the vote count
        candidate_name = row[2] 
        if candidate_name not in names:
            names.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name]+=1

#export
output = os.path.join("analysis", "election_analysis.txt")
with open(output,'w')as file:

    # total vote info
    vote_results = (
        "Election Results\n"
        "------------------------\n"
        f"Total votes: {votes}\n"
        "------------------------\n"
    )
    print(vote_results)
    file.write(vote_results)

    # candidate vote counts and percentages and update winner info
    for candidate in candidate_votes:
        vote_count = candidate_votes.get(candidate)
        vote_percent = float(vote_count)/votes*100
        if vote_count > winner_count:
            winner_count = vote_count
            winner = candidate

        #formatting
        candidate_results = f"{candidate}: {vote_percent:.3f}% ({vote_count})\n"
        print(candidate_results)
        file.write(candidate_results)
    
    # winner info
    winner_result = (
f"""-------------------------
Winner: {winner}
-------------------------"""
    )
    print(winner_result)
    file.write(winner_result)