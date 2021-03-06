# Import pandas
import pandas as pd
import os

# Read polling csv
df_polling_results = pd.read_csv("election_results.csv")

# Analysis to run:

# Total number of votes cast
total_votes = 0

for ID in df_polling_results["Ballot ID"]:
    total_votes += 1

# Make complete list of counties that voted in the election
voting_counties = []

# Make dictionary to match county with number of votes cast
votes_by_county = {}

for county in df_polling_results["County"]:
    if county not in voting_counties:
        voting_counties.append(county)
        votes_by_county[county] = 0

    votes_by_county[county] += 1

# Determine the county that submitted the most votes
# Set variables
county_most_votes = ""
count_county_most_votes = 0
percentage_county_most_votes = 0

# Find percentage of total votes that each county had
for county in votes_by_county:
    county_votes = votes_by_county[county]
    percentage_county_votes = (county_votes / total_votes) * 100

     # Find the county that submitted the most votes
    if votes_by_county[county] > count_county_most_votes and percentage_county_votes > percentage_county_most_votes:
        county_most_votes = county
        count_county_most_votes = votes_by_county[county]
        percentage_county_most_votes = percentage_county_votes

# Make a list of candidates
candidate_options = []

# Make a dictionary pairing each candidate to the number of votes they received
candidate_votes = {}

for name in df_polling_results["Candidate"]:
    if name not in candidate_options:
        candidate_options.append(name)

        candidate_votes[name] = 0
    candidate_votes[name] += 1


# Find percentage of votes each candidate received in order to determine the election winner 
# Set variables   
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Find percentage votes
for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percentage = (votes / total_votes) * 100

    # Determine the winner of the election based on popular vote
    if candidate_votes[name] > winning_count and vote_percentage > winning_percentage:
        winning_count = candidate_votes[name]
        winning_percentage = vote_percentage
        winning_candidate = name

# Print layouts for terminal and text file where you will write election results
election_summary_for_txtfile = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n")

election_summary_for_print = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

winning_candidate_summary_for_txtfile = (
    "\n"
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")

winning_candidate_summary_for_print = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------")

# PRINT ELECTION RESULTS TO TERMINAL
# general summary
print(election_summary_for_print)

# election breakdown by county
for county in votes_by_county:
    county_votes = votes_by_county[county]
    percentage_county_votes = (county_votes / total_votes) * 100
    county_results = f"{county}: {percentage_county_votes:.1f}% ({county_votes:,})\n"
    print(county_results)

print(
    f"-------------------------\n"
    f"Largest County Turnout: {county_most_votes}\n"
    f"-------------------------\n"
    )

# election breakdown by candidate
for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percentage = (votes / total_votes) * 100
    candidate_results = (f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
    print(candidate_results)

print(winning_candidate_summary_for_print)

# TRANSFER ELECTION RESULTS TO TEXT FILE
# Set the file you are going to write on
file_to_save = open(r"C:\Users\candy\OneDrive\Documents\Bootcamp\Module 3\Election Analysis\Election_Analysis\Analysis\election_analysis.txt", "w")
# Write inside file
# general election results
file_to_save.write(election_summary_for_txtfile)

# election breakdown by county
for county in votes_by_county:
    county_votes = votes_by_county[county]
    percentage_county_votes = (county_votes / total_votes) * 100
    county_results = f"{county}: {percentage_county_votes:.1f}% ({county_votes:,})\n"
    file_to_save.write(county_results)

file_to_save.write(
    "\n"
    f"-------------------------\n"
    f"Largest County Turnout: {county_most_votes}\n"
    f"-------------------------\n\n"
    )


# election breakdown by candidate
for name in candidate_votes:
    votes = candidate_votes[name]
    vote_percentage = (votes / total_votes) * 100
    candidate_results = (f"{name}: {vote_percentage:.1f}% ({votes:,})\n")
    file_to_save.write(candidate_results)

file_to_save.write(winning_candidate_summary_for_txtfile)
# Close the file
file_to_save.close()  
