import csv

with open('u.data.csv') as import_file: # automatically closes the file when done
    reader = csv.reader(import_file, delimiter='\t')
    headers = next(reader)
    print(headers)
    print('------')
    for row in reader:
        print(row)
