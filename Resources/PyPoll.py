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
print(df_polling_results.head())

# Analysis to run:
# Total number of votes cast
total_votes = 0

for ID in df_polling_results["Ballot ID"]:
    total_votes += 1

print(total_votes)

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


print(candidate_options)
print(candidate_votes)


# Percentage of votes each candidate won

# The winner of the election based on popular vote