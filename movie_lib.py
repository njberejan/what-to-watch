import csv

# u.data.csv key = user id | item id | rating | timestamp
# u.data.csv index=   [0]  |   [1]   |   [2]  |   [3]

class Movie:

    def __init__(self, dict):
# movie id | movie title | release date | video release date |
# IMDb URL

        self.movie_movie_id = dict['movie_id']
        self.movie_movie_title = dict['movie_title']
        self.movie_release_date = dict['release_date']
        self.movie_video_release_date = dict['video_release_date']
        self.movie_imdb_url = dict['IMDb_URL']


class User:

    def __init__(self, dict):
        self.user_user_id = dict['user_id']
        self.user_age = dict['age']
        self.user_gender = dict['gender']
        self.user_occupation = dict['occupation']
        self.user_zip_code = dict['zip_code']

class Rating:

    def __init__(self, dict):
        self.rating_user_id = dict['user_id']
        self.rating_item_id = dict['item_id']
        self.rating_rating = dict['rating']
        self.rating_timestamp = dict['timestamp']

data_list = []

with open('u.item.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='|')
    for row in reader:
        test = Movie(row)
        data_list.append(test)
    print(data_list)

with open('u.user.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='|')
    for row in reader:
        test = User(row)
    #     data_list.append(test)
    # print(data_list)

with open('u.data.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='\t')
    for row in reader:
        test = Rating(row)
    #     data_list.append(test)
    # print(data_list)
