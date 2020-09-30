import os
import csv

poll_csv = os.path.join("/Users/katrinasmith/Desktop/Bootcamp/Homework/KSmith_PythonChallenge/PyPoll/Resources/election_data.csv

# read in CSV file
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# remove header
    csv_header = next(csvfile)

# list and define variables
voter_id [0]
County [1]
Candidate [2]
# calculate total number of votes cast
total_votes = (voter_id + 1)
# calculate a list of candidates who received votes
candidates = 

# calculate number of votes each candidate won
# need to create a calulation per candidate
total_ = total_votes.count()

# calculate percentage of votes each candidate won
# need to create a calculation per candidate
percent_ = (total_ /total_votes)

# calculate the winner of the election based on popular vote
winner = 
# print results to a terminal and export a text file with results
print(f"Total Number of Votes: {int(total_votes)}")
print(f"Candidates: {str(candidates)}")
print(f"Percentage per Candidate: {int(percent)}")
print(f"Total Votes per Candidate: {int(total)}")
print(f"Winner: {str(winner}")