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
#supposed to print movie ID where movie id and rating id match. Does not.
    # def average_rating(self, movie_list):
    #     for rating in rating_list:
    #         print(rating.rating_item_id)
    #         if rating.rating_item_id == movie.movie_movie_id:
    #             print(movie.movie_movie_id)

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

    def __str__(self):
        return str(self.rating_item_id)
        return str(self.rating_rating)

    def gets_all_ratings(self, dict):
        for rating.rating_item_id in rating_list:
            test_list = []
            test_list.append(rating.rating_rating)
            print(test_list[0])
    # def gets_average_rating(self, dict):


movie_list = []
user_list = []
rating_list = []
all_ratings_for_movie = []
with open('u.item.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='|')
    for row in reader:
        movie = Movie(row)
        #creates instance of object with attributes as keys to dictionary values
        movie_list.append(movie)
    # print(movie_list)

with open('u.user.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='|')
    for row in reader:
        user = User(row)
        user_list.append(user)
    # print(user_list)

with open('u.data.csv') as import_file: # automatically closes the file when done
    reader = csv.DictReader(import_file, delimiter='\t')
    for row in reader:
        rating = Rating(row)
        rating_list.append(rating)
    # print(rating_list)

# Movie.average_rating(movie, movie_list)
Rating.gets_all_ratings(rating, rating_list)
print(movie_list)
#try this with list import instead of dictionary import
