import csv
class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title

    def __str__(self):
        return '{}: {}'.format(self.id, self.title)

    def movies_listed_by_title(self):
        movies_list = [movies[key] for key in movies]
        user_input = input('Enter part of a movie title: ').lower()
        for movie in movies_list:
            if user_input in movie.title.lower():
                print(movie)

    def find_title_by_id(self):
        key = input('Enter the movie ID number: ')
        print(movies.get(key))


class User:
	def __init__(self, user_id, age, gender, occupation, zip_code):
		self.id = user_id
		self.age = age
		self.gender = gender
		self.occupation = occupation
		self.zip_code = zip_code

	def __str__(self):
		return 'ID: {}, Age: {}, Gender: {}, Occupation {}, Zip Code: {}'.format(self.id, self.age, self.gender, self.occupation, self.zip_code)

class Rating:

    def __init__(self, row):
        self.id = row[0]
        self.item_id = row[1]
        self.rating = row[2]

    def __str__(self):
        return 'User ID: {}, Item ID: {}, Rating: {}'.format(self.id, self.item_id, self.rating)

    def find_all_ratings_by_userid(ratings_data_list):
        #returns dictionary with key User ID and value list of all reviews from user
        user_dict = {}
        user_list = []
        user_id = input("Please enter a User ID number: ")
        for objects in ratings_data_list:
            if objects.id == user_id:
                user_list.append(objects.rating)
        user_dict[user_id] = user_list
        all_user_ratings = user_dict
        return all_user_ratings

    def find_all_ratings_by_movieid(ratings_data_list):
        #returns dictionary with key Movie ID and value list of all reviews for movie
        ratings_dict = {}
        ratings_list = []
        movie_id = input("Please enter a Movie ID number: ")
        for objects in ratings_data_list:
            if objects.item_id == movie_id:
                ratings_list.append(int(objects.rating))
            ratings_dict[movie_id] = ratings_list
        all_ratings_by_movieid = ratings_dict
        return all_ratings_by_movieid, movie_id, ratings_list

    def find_average_rating_by_movieid(ratings_list):
        #returns average rating for movie by movie ID. Must first run find_all_ratings_by_movieid, however.
        average_rating_by_movieid = sum(ratings_list) / int(len(ratings_list))
        return average_rating_by_movieid

movies = {}
with open('u.item.csv', encoding='latin_1') as item_file:
    reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    for row in reader:
        movie = Movie(row['movie_id'], row['title'])
        movies[movie.id] = movie #creates dict "movies" with the movie ID as the key and the title as the value
    # print(movie)

users = {}
with open('u.user.csv', encoding='latin_1') as user_file:
    reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    for row in reader:
        user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
        users[user.id] = user #creates dictionary "users" with user ID as the key and THE OBJECT AS THE VALUE
    # print(users['1'])
    # print(users['1'].occupation)

ratings_data_list = []
with open('u.data.csv', encoding='latin_1') as ratings_file: #CREATES LIST OF EACH LINE AS A LIST
    reader = csv.reader(ratings_file, delimiter='\t')
    head = next(reader)
    for row in reader:
        rating = Rating(row)
        ratings_data_list.append(rating)

print(ratings_data_list[0])
all_ratings_by_user = Rating.find_all_ratings_by_userid(ratings_data_list)
print(all_ratings_by_user)
all_ratings_by_movie, movie_id, ratings_list = Rating.find_all_ratings_by_movieid(ratings_data_list)
print(all_ratings_by_movie)
average_by_movie = Rating.find_average_rating_by_movieid(ratings_list)
print(average_by_movie)
