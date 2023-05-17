import os
import csv

# Set path for csv file
election_data_csv = os.path.join("resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    header = next(csvreader)

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate name from the row
        candidate_name = row[2]

        # If the candidate already exists in the dictionary, increment their vote count
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            # If the candidate is not present in the dictionary, add them with an initial vote count of 1
            candidates[candidate_name] = 1

# Determine the winner
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Calculate the percentage of votes for each candidate
candidate_percentages = {}
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidate_percentages[candidate] = percentage

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage in candidate_percentages.items():
    print(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_file = "election_results.txt"
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, percentage in candidate_percentages.items():
        file.write(f"{candidate}: {percentage:.3f}% ({candidates[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

print(f"Analysis has been saved to {output_file}.")
