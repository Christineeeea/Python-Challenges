import os 
import csv

csvpath = os.path.join('budget_data_1.csv')

date = []
revenue = []

with open (csvpath, 'r', newline='') as budget_data:
    csvreader = csv.reader(budget_data, delimiter = ',')
    month = list(csvreader)
    row_count = len(month)


    for row in csvreader:
        date.append(row[1])
        revenue.append(row[2])

print ('Financial Analysis')
print ('--------------------------------')
print ('Total Months: ', row_count)

Total_Revenue = 0 
for i in revenue:
    Total_Revenue += int(i)

print('Total Revenue: ' + '$' + str(Total_Revenue))


greatest = 0
for b in range(len(revenue)):
    if int(revenue[b])-int(revenue[b-1])> greatest:
        greatest = int(revenue[b]) - int(revenue[b-1])
        greatest_month = date[b]

worst = 0
for c in range(len(revenue)):
    if int(revenue[c]) - int(revenue[c-1]) < worst:
        worst = int(revenue[c]) - int(revenue(c-1))
        worst_month = date[c]

print('Greatest Increase in Revenue: ',  greatest_month, ' ('+'$'+str(greatest)+')')
print('Greatest Decrease in Revenue: ',  worst_month, ' ('+'$'+str(worst)+')')


bank_data = zip(date, revenue)
monthly_change = [(x-y)/2.0 for (x,y) in zip(revenue[:1], revenue[-1:])]
monthly_change_sum = 0
for a in range(row_count):
    monthly_change_sum += int(revenue[a]-int(revenue[a-1]))
    revenue_change = mean (monthly_change_sum)
    print('Average Revenue Change: $' + str(revenue_change))

txtpath = os.path.join('summary_budget1.txt')
    with open (txtpath, 'w', newline = '') as summary_pybank:
        writer = csv.writer(summary_pybank)
        writer.writerrows['Financial Analysis'],
                         ['----------------------']
                         ['"Total Months: '+str(row_count)]
                         ["Total Revenue: "+str(total_revenue)]
                         ['Average Revenue Change'+str(revenue_change)]






