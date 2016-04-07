import csv

# u.data.csv key = user id | item id | rating | timestamp
# u.data.csv index=   [0]  |   [1]   |   [2]  |   [3]

# class Movie:
#
#     def __init__(self):
#
#
#
class User:
#user_id|age|gender|occupation|zip_code
    def __init__(self):
        self.user_user_id =
        self.user_age =
        self.gender =
        self.occupation =
        self.zip_code =


class Rating:

    def __init__(self, dict):
        self.rating_user_id = dict['user_id']
        self.rating_item_id = dict['item_id']
        self.rating = dict['rating']
        self.timestamp = dict['timestamp']

data_list = []

with open('u.data.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='\t')
    for row in reader:
        test = Rating(row)
        data_list.append(test)
    print(data_list)

with open('u.data.csv') as import_file: # automatically closes the file when done
    reader = csv.reader(import_file, delimiter='\t')
    headers = next(reader)
    print(headers)
    print('------')
    for row in reader:
        headers = ['user_id', 'item_id', 'rating', 'timestamp']
