import csv
file = open('main.csv')
reader = csv.reader(file)
for line in reader:
    print(line)