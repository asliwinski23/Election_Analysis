# Import pandas
import pandas as pd
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = open(r"C:\Users\candy\OneDrive\Documents\Bootcamp\Module 3\Election Analysis\Election_Analysis\Analysis\election_analysis.txt", "w")
# Write inside file
file_to_save.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
# Close the file
file_to_save.close()  


# Read polling csv
df_polling_results = pd.read_csv("election_results.csv")
# print(df_polling_results.head())

# Analysis to run:
# Total number of votes cast
total_votes = 0

for ID in df_polling_results["Ballot ID"]:
    total_votes += 1

# print(total_votes)

# Wrote total number of votes to text file

# A complete list of candidates who received votes
candidate_options = []

#Total number of votes each candidate received
candidate_votes = {}

for name in df_polling_results["Candidate"]:
    if name not in candidate_options:
        candidate_options.append(name)

        candidate_votes[name] = 0
    candidate_votes[name] += 1

# print(candidate_options)
print(candidate_votes)

  # Percentage of votes each candidate won
winning_candidate = ""
winning_count = 0
winning_percentage = 0

for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percentage = (votes / total_votes) * 100
    # print(f"{name}: received {vote_percentage:.2f}% of the vote.")

# The winner of the election based on popular vote
    if candidate_votes[name] > winning_count and vote_percentage > winning_percentage:
        winning_count = candidate_votes[name]
        winning_percentage = vote_percentage
        winning_candidate = name
    
    # print(f"{name}: {vote_percentage:.1f}% ({votes:,})\n")

election_summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

# print(election_summary)
# print(winning_candidate_summary)
# with open(file_to_save, "w") as txt_file:
#     file_to_save.write(winning_candidate_summary)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = open(r"C:\Users\candy\OneDrive\Documents\Bootcamp\Module 3\Election Analysis\Election_Analysis\Analysis\election_analysis.txt", "w")
# Write inside file
file_to_save.write(election_summary)
for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percentage = (votes / total_votes) * 100
    candidate_results = (f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
    file_to_save.write(candidate_results)
file_to_save.write(winning_candidate_summary)
# Close the file
file_to_save.close()  
