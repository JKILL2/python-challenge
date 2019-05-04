import csv
import os

# define path of csv file and output file
data_file = os.path.join("Resources", "election_data.csv")
output = os.path.join("Analysis.txt")

# set vaiables
total_votes = 0
candidate_list = []
votes_by_candidate = {}
vote_winner = 0

# open the csv file with voting data
with open(data_file) as data:
    table = csv.reader(data)
    header = next(table)
    
    # go row by row and count each vote
    for row in table:
        
        # add to total number of votes
        total_votes += 1
        name = row[2]

        #if candidate has other votes then add to vote tally
        if name not in candidate_list:
            candidate_list.append(name)
            votes_by_candidate[name] = 0
        
        #if not, create new spot in list for candidate
        votes_by_candidate[name] += 1

# print out total votes
results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
print(results)

with open(output, "w") as txt_file:
    txt_file.write(results)

    #find percentage of vote for each candidate and the winner
    for name in votes_by_candidate:
        votes_count = votes_by_candidate.get(name)
        vote_percentage = (float(votes_count) / float(total_votes)) * 100

        if votes_count > vote_winner:
            vote_winner = votes_count
            winner = name
        
        #print results
        results_2 = f"{name}: {vote_percentage:.3f}% ({votes_count})\n"
        print(results_2, end="")

        txt_file.write(results_2)

    # print winner's name
    results_3 = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n")
    print(results_3)

    txt_file.write(results_3)