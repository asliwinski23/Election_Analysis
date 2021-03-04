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

# A complete list of candidates who received votes

# Total number of votes each candidate received

# Percentage of votes each candidate won

# The winner of the election based on popular vote