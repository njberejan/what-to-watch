import csv

class Movie:

    def __init__(self, movie_id, movie_title):
# movie id | movie title | release date | video release date |
# IMDb URL
        self.movie_movie_id = movie_id
        self.movie_movie_title = movie_title

    def __str__(self):
        return "movie_id: " + str(self.movie_movie_id) + " movie_title: " + str(self.movie_movie_title) + " release_date: " + str(self.movie_release_date) + " IMDb_URL: " + str(self.movie_imdb_url)

class User:

    def __init__(self, list):
        self.user_user_id = user_id
        self.user_age = age
        self.user_gender = gender
        self.user_occupation = occupation
        self.user_zip_code = zip_code

    def __str__(self):
        return "user_id: " + str(self.user_user_id) + " age: " + str(self.user_age) + " gender: " + str(self.user_gender) + " occupation: " + str(self.user_occupation) + " zip_code: " + str(self.user_zip_code)

class Rating:

    def __init__(self, list):
        self.rating_user_id = user_id
        self.rating_item_id = item_id
        self.rating_rating = rating
        self.rating_timestamp = timestamp

    def __str__(self):
        return "user_id: " + str(self.rating_user_id) + " item_id: " + str(self.rating_item_id) + " rating: " + str(self.rating_rating) + " timestamp: " + str(self.rating_timestamp)


movie_list = []
user_list = []
rating_list = []
all_ratings_for_movie = []

with open('u.item.csv', encoding='latin_1') as import_item_file: # automatically closes the file when done
    reader = csv.reader(import_item_file,  delimiter='|')
    for row in reader:
        movie_list.append(Movie(row))
    print(movie_list)

with open('u.user.csv', encoding='latin_1') as import_user_file: # automatically closes the file when done
    reader = csv.reader(import_user_file, delimiter='|')
    for row in reader:
        user_list.append(User(row))
    # print(user_list)

with open('u.data.csv', encoding='latin_1') as import_data_file: # automatically closes the file when done
    reader = csv.reader(import_data_file, delimiter='\t')
    for row in reader:
        rating_list.append(Rating(row))
    # print(rating_list)
