import os
import csv

poll_csv = os.path.join("Resources/election_data.csv")

total_votes = []
candidates = []
candidates_unique = []
# read in CSV file
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# remove header
    csv_header = next(csvreader)


# calculate total number of votes cast

    for row in csvreader:

        total_votes.append(row[0])
        candidates.append(row[2])
    # calculate a list of candidates who received votes
    for name in candidates:
        if name not in candidates_unique:
            candidates_unique.append(name)


print("Election Results")
print("----------------")
print(f"Total Votes: {len(total_votes)}")
print("----------------")
for name in candidates_unique:
    print(f"{name}:  {(candidates.count(name)/len(total_votes))* 100:.3f}%  ({candidates.count(name)})")
print("----------------")
print(f"Winner:  {max(set(candidates), key=candidates.count)}")

output_path = "Analysis/Results.txt"
with open(output_path, 'w') as output_file:
    csvwriter = csv.writer(output_file)
    output_file.write(
    "Election Results" 
    "\n"
    "----------------" 
    "\n"
    f"Total Votes: {len(total_votes)}"
    "\n"
    "----------------"
    "\n" )
    for name in candidates_unique:
        output_file.write(f"{name}:  {(candidates.count(name)/len(total_votes))* 100:.3f}%  ({candidates.count(name)})\n")
    output_file.write(
    "----------------"
    "\n"
    f"Winner:  {max(set(candidates), key=candidates.count)}"

        )