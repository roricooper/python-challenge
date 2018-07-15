# pypoll
# dependencies
import os
import csv
import pandas as pd

#files to load and output
file_to_load = os.path.join("..", "PyPoll","election_data.csv")
file_to_save = os.path.join("..", "PyPoll", "election_results.txt")
#print(file_to_load)
#print(file_to_save)

df = pd.read_csv(file_to_load)
#print(df)

df.columns = ["Voter ID", "County", "Candidate"]
#print(df.columns)

df.shape
#print(df.shape)

df.head()
#print ("Rori Cooper - Unit 3 Assignment")
#print ("")
title = str("Outcome of PyPoll Election")

print(f"{title}")
print("--------------------------------------")

#sum of rows before loop starts
GrandTotalVotes = len(df)
print(GrandTotalVotes)

#counters for loop
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0

#loop
with open("election_data.csv") as election_data:
    reader = csv.reader(election_data)
    next(reader)
    #print(header)
    for row in reader:
        #print(row)
        candidate_votes
        total_votes= total_votes + 1
        candidate_name = row [2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #print(candidate_options)
            candidate_votes[candidate_name] = 0
            #print(candidate_votes)
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print(candidate_votes)
for candidate in candidate_votes:
        #print('----------------------------------------------------')
        #print(total_votes)
        #print(candidate)
        #print(candidate_votes.get(candidate))
        votes = (candidate_votes.get(candidate))
        vote_percentage = float(votes)/float(total_votes)*100

        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        voter_output = f"{candidate}: {vote_percentage: .3f}% ({votes})\n"
        print(voter_output, end="")
        finalsummary = f"{voter_output}\n"
        #print(finalsummary)

candidate_votes.keys()
election_results = (
        "f\n\Election Results\n"
        "f\n-----------------------\n")
election_results
electionR = f"Election Results: {total_votes}"
#print(electionR)



#txt_file.write(file_to_save)

winning_candidate_summary = (
    f"\n-------------------------------\n"
    f"\nGrand Total Votes: {GrandTotalVotes}\n"
    f"\n-------------------------------\n"
    f"\n{finalsummary}\n"
    f"\n-------------------------------\n"
    f"\nWinner: {winning_candidate}\n"
    f"\n-------------------------------\n")
print(winning_candidate_summary)




with open(file_to_save, "w") as txt_file:
    txt_file.write(winning_candidate_summary)
