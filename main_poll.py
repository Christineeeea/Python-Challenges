import os
import csv

csvpath = os.path.join('election_data1.csv')
candidates = []
total_votes = []


with open (csvpath, newline = '') as election_data:
    reader = csv.reader(election_data, delimiter=',')

    next(reader)

    row_count=0
    for row in reader:
            total_votes.append(row[2])
            row_count += 1

            