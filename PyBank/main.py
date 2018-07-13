# pybank
# dependencies
import os
import csv

#files to load and output
file_to_load = os.path.join("..", "PyBank","budget_data.csv")
file_to_save = os.path.join("..", "PyBank", "analysis_data.txt")


prevRevenue = 0
totalNumMonths = 0
totalRevenue = 0
MonthofGreatestIncrease = ""
greatestIncrease = 0
MonthofGreatestDecrease = ""
greatestDecrease = 0

with open(file_to_load) as raw_data:
    raw_data_read = csv.reader(raw_data)
    next(raw_data_read)

    for row in raw_data_read:
        totalNumMonths+=1

        thisMonth = row[0]
        thisRevenue = int(row[1])

        RevenueChange= thisRevenue - prevRevenue

        if RevenueChange > greatestIncrease:
            MonthofGreatestIncrease = thisMonth
            GreatestIncrease = RevenueChange

        if RevenueChange < greatestDecrease:
            MontofGreatestDecrease = thisMonth
            GreatestDecrease = RevenueChange

        prevRevenue = thisRevenue

        totalRevenue += thisRevenue

    AverageRevenue = totalRevenue/totalNumMonths

print("Rori Cooper - Unit 3 Assignment")
print("")
print("Financial Analysis of PyBank")
print("-----------------------------------------------")
print(f"Total Number of Months: {totalNumMonths} months")
print(f"Total Revenue: ${totalRevenue}")
print(f"Average Change: ${AverageRevenue}")
print(f"Greatest Increase in Revenue: {MonthofGreatestIncrease} ${GreatestIncrease}")
print(f"Greatest Decrease in Revenue: {MontofGreatestDecrease} ${GreatestDecrease}")
print("------------------------------------------------")

output = (
    f"\nRori Cooper - Unit 3 Assignment\n"
    f"\n\n"
    f"\nFinancial Analysis\n"
    f"\n-----------------------------------------------\n"
    f"\nTotal Number of Months: {totalNumMonths} months\n"
    f"\nTotal Revenue: ${totalRevenue}\n"
    f"\nAverage Change: ${AverageRevenue}\n"
    f"\nGreatest Increase in Revenue: {MonthofGreatestIncrease} ${GreatestIncrease}\n"
    f"\nGreatest Decrease in Revenue: {MontofGreatestDecrease} ${GreatestDecrease}\n"
    f"\n------------------------------------------------\n")
print(output)
with open(file_to_save, "w") as txt_file:
    txt_file.write(output)

