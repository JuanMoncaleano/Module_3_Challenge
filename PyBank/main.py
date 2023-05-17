import os
import csv

# Set path for csv file
budget_data_csv = os.path.join("resources", "budget_data.csv")

# Define variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# Read csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    header = next(csvreader)

    # Process data
    for row in csvreader:
        # Count total number of months
        total_months += 1

        # Calculate Net total amount of "Profit/Losses"
        net_total += int(row[1])

        # Calculate the change in "Profit/Losses"
        if total_months > 1:
            change = int(row[1]) - previous_profit_loss
            total_change += change

            # Check if the change is the greatest increase or decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        # Store the current month's "Profit/Losses"
        previous_profit_loss = int(row[1])

# Calculate average change
average_change = total_change / (total_months - 1)

# Format the output
analysis_output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})
"""

# Print the analysis to the terminal
print(analysis_output)

# Export the analysis to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as textfile:
    textfile.write(analysis_output)

print(f"Analysis exported to {output_file} successfully.")
