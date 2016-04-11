import csv
import operator
class Movie:
	def __init__(self, movie_id, title, movie_ratings_dict):
		self.id = movie_id
		self.title = title
		self.ratings = movie_ratings_dict

	def __str__(self):
		return '{}: {}'.format(self.id, self.title)

	def movies_listed_by_title(self):
		movies_list = [movies[key] for key in movies]
		user_input = input('Enter part of a movie title: ').lower()
		for movie in movies_list:
			if user_input in movie.title.lower():
				print(movie)

	def find_title_by_id(self):
		key = int(input('Enter the movie ID number: '))
		print(movie_dict.get(key))

	def get_all_ratings_for_a_movie(self, movie_dict):
		all_ratings_dict = {}
		for movie_id in movie_dict:
			movie = movie_dict[movie_id]
			ratings = []
			for rating in movie.ratings:
				ratings.append(rating[1])
				all_ratings_dict[movie_id] = ratings
		return all_ratings_dict

	def get_average_score_for_every_movie(self, all_ratings_dict):
		all_average_scores_dict = {}
		for movie_id, ratings in all_ratings_dict.items():
			average_score = []
			average_score.append(sum(ratings) / len(ratings))
			all_average_scores_dict[movie_id] = average_score
		return all_average_scores_dict

class User:
	def __init__(self, user_id, age, gender, occupation, zip_code):
		self.id = user_id
		self.age = age
		self.gender = gender
		self.occupation = occupation
		self.zip_code = zip_code

	def __str__(self):
		return 'ID: {}, Age: {}, Gender: {}, Occupation {}, Zip Code: {}'.format(self.id, self.age, self.gender, self.occupation, self.zip_code)

users = {}
with open('u.user.csv', encoding='latin_1') as user_file:
    reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    for row in reader:
        user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
        users[user.id] = user #creates dictionary "users" with user ID as the key and THE OBJECT AS THE VALUE
    # print(users['1'])
    # print(users['1'].occupation)


def gets_ratings_file_data():
	with open('u.data.csv', encoding='latin_1') as ratings_file:
		reader = csv.DictReader(ratings_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating', 'timestamp'])
		movie_ratings_dict = {}
		for row in reader:
			if int(row['movie_id']) in movie_ratings_dict:
				movie_ratings_dict[int(row['movie_id'])].append((int(row['user_id']), int(row['rating'])))
			else:
				movie_ratings_dict[int(row['movie_id'])] = [(int(row['user_id']), int(row['rating']))]
				#imports file and returns dictionary with item id as the key and a list of user id and corresponding review score tuples.
		return movie_ratings_dict

def gets_item_file_data(movie_ratings_dict):
	with open('u.item.csv', encoding='latin_1') as item_file:
		reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
		movie_dict = {}
		for row in reader:
			movie_dict[int(row['movie_id'])] = Movie(row['movie_id'], row['title'], movie_ratings_dict[int(row['movie_id'])])
		return movie_dict
    # print(movie)


movie_ratings_dict = gets_ratings_file_data()
# print(movie_ratings_dict)
movie_dict = gets_item_file_data(movie_ratings_dict)
all_ratings_dict = Movie.get_all_ratings_for_a_movie(Movie, movie_dict)
# print(all_ratings_dict)
all_average_scores_dict = Movie.get_average_score_for_every_movie(Movie, all_ratings_dict)
# print(all_average_scores_dict)

sorted_averages = sorted(all_average_scores_dict.items(), key=operator.itemgetter(1))
print(sorted_averages)
Movie.find_title_by_id(Movie)
#print debugging stuff
# movie = movie_dict[123]
# print(movie.ratings)
# print(movie.ratings[0])
# print(movie.ratings[0][1])
# Movie.get_all_ratings_for_a_movie(Movie)
