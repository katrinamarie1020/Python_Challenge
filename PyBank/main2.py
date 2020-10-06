# import my csv file
import os
import csv

bank_csv = os.path.join("Resources/budget_data.csv")

months = 0
profit_loss = 0
change = []
total_change = 0
max_change = 0
max_decrease = 0

# read in CSV file
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove header
    csv_header = next(csvfile)

    for row in csvreader:

        # lists to store the data
        months = months + 1

        profit_loss = int(row[1]) + profit_loss

        if row[0] == "Jan-2010":
            pass
        else:
            change = int(row[1]) - prev_value

            total_change = change + total_change

            if max_change < change:
                max_change = change 
                max_month = row[0]

            if max_decrease > change:
                max_decrease = change 
                max_dec_month = row[0]

        prev_value = int(row[1]) 

 
print(f"Total Number of Months: {int(months)}")
print(f"Net Total: {int(profit_loss)}")
print(f"Greatest Increase: {(max_month, max_change)}")
print(f"Greatest Decrease: {(max_dec_month, max_decrease)}")

output_path = "Analysis/Results.txt"
with open(output_path, 'w') as output_file:
    csvwriter = csv.writer(output_file)
    output_file.write(
    "Financial Analysis" 
    "\n"
    "----------------" 
    "\n"
    f"Total Number of Months: {int(months)}"
    "\n"
    f"Net Total: {int(profit_loss)}"
    "\n" 
    f"Greatest Increase: {(max_month, max_change)}"
    "\n"
    f"Greatest Decrease: {(max_dec_month, max_decrease)}"

        )