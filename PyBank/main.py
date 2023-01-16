import os
import csv

months = []
profit = []
total = []

filepath = os.path.join('..','Resources/budget_data.csv')

with open(filepath, 'r') as csvfile:
    file = csv.reader(csvfile, delimiter=",")
    next(file, None)

    for row in file:
        total.append(int(row[1]))
        months.append(row[0])

for x in range(85):
    prof = total[x+1] - total[x]
    profit.append(prof)


max_profit = max(profit)
max_profit_index = profit.index(max_profit)
min_profit = min(profit)
min_profit_index = profit.index(min_profit)
num_months = (len(set(months)))

print("Financial Analysis")
print("---------------------------------")
print("Number of Months:" + str(num_months))
print("Total: $" + str(sum(total)))
print("Average Change: $" + str((mean(profit), 2)))
print("Greatest Increase in Profits: " + str(months[max__profit_index+1]) + "$" + str(max_profit))
print("Greatest Decrease in Profits: " + str(months[min_profit_index+1]) + "$" + str(min_profit))