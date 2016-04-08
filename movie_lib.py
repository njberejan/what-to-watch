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

    def __str__(self):
        return "movie_id: " + str(self.movie_movie_id) + " movie_title: " + str(self.movie_movie_title) + " release_date: " + str(self.movie_release_date) + " IMDb_URL: " + str(self.movie_imdb_url)

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

    def __str__(self):
        return "user_id: " + str(self.user_user_id) + " age: " + str(self.user_age) + " gender: " + str(self.user_gender) + " occupation: " + str(self.user_occupation) + " zip_code: " + str(self.user_zip_code)

class Rating:

    def __init__(self, dict):
        self.rating_user_id = dict['user_id']
        self.rating_item_id = dict['item_id']
        self.rating_rating = dict['rating']
        self.rating_timestamp = dict['timestamp']

    def __str__(self):
        return "user_id: " + str(self.rating_user_id) + " item_id: " + str(self.rating_item_id) + " rating: " + str(self.rating_rating) + " timestamp: " + str(self.rating_timestamp)

    # def gets_all_ratings(self, dict):
    #     #returns just list of 3s right now.
    #     test_list = []
    #     for self.rating_item_id in rating_list:
    #         test_list.append(self.rating_rating)
    #     print(len(test_list))
    # # def gets_average_rating(self, dict):


movie_list = []
user_list = []
rating_list = []
all_ratings_for_movie = []

with open('u.item.csv') as import_item_file: # automatically closes the file when done
    reader = csv.DictReader(import_item_file, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
    for row in reader:
        # movie = Movie(row)
        movie_list.append(Movie(row))
    # print(movie_list)

with open('u.user.csv') as import_user_file: # automatically closes the file when done
    reader = csv.DictReader(import_user_file, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
    for row in reader:
        # user = User(row)
        user_list.append(User(row))
    # print(user_list)

with open('u.data.csv') as import_data_file: # automatically closes the file when done
    reader = csv.DictReader(import_data_file, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='\t')
    for row in reader:
        # rating = Rating(row)
        rating_list.append(Rating(row))
    # print(rating_list)

# Movie.average_rating(movie, movie_list)
# Rating.gets_all_ratings(Rating(row), rating_list)
# for rating in rating_list:
print('Rating List: ' + str(rating_list[0])) #prints the item_id of the indexed object. Why not other aspects of object?
print('User List: ' + str(user_list[0]))
print('Movie List: ' + str(movie_list[0]))
test_list = []

for Rating.rating_item_id in rating_list:
    if Rating['item_id'] == 242:
        print("hi")
#         test_list.append(Rating.get('rating'))
# print(test_list)

with open('u.item.csv') as import_item_file: # automatically closes the file when done
    reader = csv.DictReader(import_item_file, fieldnames=['movie_id', 'movie_title', '', '', 'something_else'], delimiter='|')
    for row in reader:
        # movie = Movie(row)
        print(row['movie_id'], row['title'])
