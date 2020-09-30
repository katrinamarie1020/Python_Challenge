# import my csv file
import os
import csv

bank_csv = os.path.join("/Users/katrinasmith/Desktop/Bootcamp/Homework/KSmith_PythonChallenge/PyBank/Resources/budget_data.csv")

months = 0
profit_loss = 0
change = []

# read in CSV file
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove header
    csv_header = next(csvfile)

    for row in csvreader:

        # lists to store the data
        months = months + 1

        profit_loss = int(row[1]) + profit_loss

# calculate total number of months in dataset
print(months)
# calculate net total amount of "profit/loss"
print(profit_loss)   

# calculate averages of changes in "profit/loss"

# calculate greatest increase in profits (date and amount)

# calculate greatest decrease in profits (date and amount)


# print analysis to terminal and export a text file with result

# print(f"Total Number of Months: {int(total_months)}")
# print(f"Net Total: {int(sum_profit_loss)}")
# print(f"Greatest Increase: {int(profit)}")
# print(f"Greatest Decrease: {int(loss)}")

