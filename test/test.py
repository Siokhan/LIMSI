import csv 
with open ('export.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
