import csv

with open('adresy.csv',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    writer = csv.writer(csvfile)
