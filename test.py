import csv

class Movie:
	def __init__(self, movie_id, title):
		self.id = movie_id
		self.title = title

	def __str__(self):
		return '{}: {}'.format(self.id, self.title)

class User:
	def __init__(self, user_id, age, gender, occupation, zip_code):
		self.id = user_id
		self.age = age
		self.gender = gender
		self.occupation = occupation
		self.zip_code = zip_code

	def __str__(self):
		return 'ID: {}, Age: {}, Gender: {}, Occupation {}, Zip Code: {}'.format(self.id, self.age, self.gender, self.occupation, self.zip_code)

movies = {}
with open('u.item.csv', encoding='latin_1') as item_file:
	reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
	for row in reader:
		movie = Movie(row['movie_id'], row['title'])
		movies[movie.id] = movie
		# print(movie)

users = {}
with open('u.user.csv', encoding='latin_1') as user_file:
	reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
	for row in reader:
		user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
		users[user.id] = user
	# print(users['2'])

# movies_list = [movies[key] for key in movies]
#
# user_input = input('Enter part of a movie title: ').lower()
#
# for movie in movies_list:
# 	if user_input in movie.title.lower():
# 		print(movie)
#
# id = input('Enter a movie id: ')

# do something with id, like look up the movie in the movies dictionary and print out the ratings for that movie, then prompt the user for input again if they want to find similar movies, etc.. etc..
