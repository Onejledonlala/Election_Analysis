# import datetime as dt
# right_now = dt.datetime.now()

# print("The time right now is ", right_now)

# import csv
# dir(csv)

# file_to_load = 'election_results.csv'
# election_data = open(file_to_load,'r')
# election_data.close()

# with open(file_to_load) as election_data:
#     print(election_data)
# Countries in the Election\n_____________________________________\nArapahoe\nDenver\nJefferson
# import csv
# import os

# file_to_save = os.path.join('election_result.txt')
# with open(file_to_save, "w") as txt_file:
#     txt_file.write('Countries in the Election\n__________________________\nArapahoe\nDenver\nJefferson')
# txt_file.close()

import csv
import os

file_to_save = os.path.join('election_result.txt')
file_to_load = os.path.join('election_results.csv')
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes +=1
        Candidate_name = row[2]
        if Candidate_name not in candidate_options:
            candidate_options.append(Candidate_name)
            candidate_votes[Candidate_name] = 0
        candidate_votes[Candidate_name] += 1
    for Candidate_name in candidate_votes:
        votes = candidate_votes[Candidate_name]
        votes_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = votes_percentage
            winning_candidate = Candidate_name
        print(f"{Candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
        winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
print(winning_candidate_summary)
     
