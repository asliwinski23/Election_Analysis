# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete an election audit of a recent local congressional election.

  1. Calculate the total number of votes cast.
  2. Get a list of counties which voted in the election.
  3. Calculate the total number of votes each county cast.
  4. Calculate the percentage of votes that came from each county.
  5. Get a complete list of candidates who received votes.
  6. Calculate the total number of votes each candidate received.
  7. Calculate the percentage of votes each candidate won.
  8. Determine the winner of the election based on popular vote.

## Resources
  * Data Source: election_results.csv
  * Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary
An analysis of the elections show that:

 * There were 369,711 votes
 * The counties were:
    *  Jefferson
    *  Denver
    *  Arapahoe
 * The county results were:
    * Jefferson county accounted for 10.5% of the total votes with 38,855 votes cast
    * Denver county accounted for 82.8% of the total votes with 306,055 votes cast
    * Arapahoe county accounted for 6.7% of the total votes with 24,801 votes cast
 * The candidate were:
    * Charles Casper Stockham
    * Diana DeGette
    * Raymon Anthony Doane
 * The candidate results were:
    * Charles Casper Stockham received 23% of the vote and 85,213 number of votes
    * Diana DeGette received 73.8% of the vote and 272,892 number of votes
    * Raymon Anthony Doane 3.1% of the vote and 11,606 number of votes

## Election Audit Summary
To make the script more flexible to any audit, a few modifications can be made. For example, it would be best to have the code prompt for a filename to analyze rather than have users paste in the unique filepath within the script every time. This accomodates users unfamiliar with the code. Furthermore, the script currently is tailored to the column headers we used in the Colorado election file. For example, the script currently calls for analysis at the county level. Thus, the lines with column references like 'County' would need to be generalized in order to read tables without county-level data.
