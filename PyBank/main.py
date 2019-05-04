import os
import csv

# define location of input and output files
csvpath = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("Resources", "Financial Analysis.txt")

# set variables
total_months = 0
total = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000000]
month_change = []
profits_change = []

# open the csv file with the data
with open(csvpath) as bud_data:
    reader = csv.reader(bud_data)
    header = next(reader)

    # count total number of months
    first_row = next(reader)
    total_months = total_months + 1
    total = total + int(first_row[1])
    prev_net = int(first_row[1])

    # go row by row and count each month
    for row in reader:
        total_months = total_months + 1
        total = total + int(row[1])

        # find the biggest and smallest change in profits
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        profits_change = profits_change + [net_change]
        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# calculate the average change in profits
net_monthly_avg = sum(profits_change) / len(profits_change)

# print out report with results
report = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total}\n"
    f"Average  Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(report)

# create output file
with open(outputfile, "w") as txt_file:
    txt_file.write(report)