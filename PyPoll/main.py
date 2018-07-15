# pypoll
# dependencies
import os
import csv
#import pandas as pd

#files to load and output
file_to_load = os.path.join("..", "PyPoll","election_data.csv")
file_to_save = os.path.join("..", "PyPoll", "election_results.txt")
#print(file_to_load)
#print(file_to_save)

#df = pd.read_csv(file_to_load)
#print(df)

#df.columns = ["Voter ID", "County", "Candidate"]
#print(df.columns)

#df.shape
#print(df.shape)

#df.head()

#myformatting
me = str ("Rori Cooper - Unit 3 Assignment")
title =(
    f"\n{me}\n"
    f"\n-------------------------------------\n")

#counters for loop
votes_count = 0
candidate_options = {}
candidate_votes_percent = {}
winning_candidate = ""
winning_count = 0

#read and loop through poll data
with open("election_data.csv") as election_data:
    reader = csv.reader(election_data)
    next(reader)

    #obtain grand total and candidate vote counts
    for row in reader:
        #print(row)
        votes_count +=1
        if row[2] in candidate_options.keys():
            candidate_options[row[2]]+=1
        else:
            candidate_options[row[2]]= 1

#obtain percentages
for key, value in candidate_options.items():
    candidate_votes_percent[key] = round((value/votes_count) * 100, 2)


#obtain winner
for key in candidate_options.keys():
    if candidate_options[key]> winning_count:
        winning_candidate = key
        winning_count = candidate_options[key]

        #hash-out later
        #print(votes_count)
        #print(candidate_options)
        #print(candidate_votes_percent)
        #print(winning_candidate)
        #print(winning_count)

#final summary print - terminal
print(f"{title}")
print("Outcome of PyPoll Election")
print("-------------------------------------")
print("Grand Total Votes: " + str(votes_count))
print("-------------------------------------")
for key, value in candidate_options.items():
    print(key + ": " + str(candidate_votes_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winning_candidate)
print("-------------------------------------")

# open txt file
file_to_save = open("election_results.txt", "w")

# write to txt file
file_to_save.write("Rori Cooper - Unit 3 Assignment\n")
file_to_save.write("-------------------------------------\n")
file_to_save.write("Outcome of PyPoll Election\n")
file_to_save.write("-------------------------------------\n")
file_to_save.write("Grand Total Votes: " + str(votes_count) + "\n")
file_to_save.write("-------------------------------------\n")
for key, value in candidate_options.items():
    file_to_save.write(key + ": " + str(candidate_votes_percent[key]) + "% (" + str(value) + ") \n")
file_to_save.write("-------------------------------------\n")
file_to_save.write("Winner: " + winning_candidate + "\n")
file_to_save.write("-------------------------------------\n")

