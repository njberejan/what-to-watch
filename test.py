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

class Rating:
	def __init__(self, user_id, item_id, rating):
		self.id = user_id
		self.item_id = item_id
		self.rating = rating

	def __str__(self):
		return 'User ID: {}, Item ID: {}, Rating: {}'.format(self.id, self.item_id, self.rating)

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
	print(users['2'])
	print(users['1'].occupation)

with open('u.data.csv', encoding='latin_1') as ratings_file: #CREATES LIST OF EACH LINE AS A LIST
	reader = csv.reader(ratings_file, delimiter='\t')
	a_list = []
	for row in reader:
		a_list.append(row)

# print(a_list[0][0]) #example of how to iterate through a list in a list to find a specific value.
# for lists in a_list:
# 	for index in lists:
# 		if index == '881250949':
# 			print(lists[2]) #this example returns the scores associated with this time stamp(useless, i know.)
#
# for lists in a_list:
# 	for index in lists:
# 		if index == '242':
# 			pass
# 			# print(lists[2]) #this example returns ALL SCORES FOR AN ITEM ID
#
# reviews = []
# for lists in a_list:
# 	for index in lists:
# 		if index == '242':
# 			reviews.append(lists[2]) #this will print  ALL SCORES FOR AN ITEM ID
# 			# print(reviews)			 #could be easily made into a function...

movies_list = [movies[key] for key in movies]
print(movies_list[0])

user_list = [users[key] for key in users]
print(user_list[0])


# ratings_list = [ratings[key] for key in ratings]
# print(ratings_list[0])
# print('ratings keys: ', ratings.keys())

# for key in ratings:
# 	print('hi')
# for key, value in movies.items(): #PRINTS MOVIE ID AND TITLE VALUES
# 	print(key, value)

# for key, value in users.items(): #PRINTS USER ID AND ALL OTHER INFO ABOUT THAT OBJECT
# 	print(key, value)

# print(movies.items()) #PRINTS KEY AND OBJECT LOCATION AS TUPLE

# user_input = input('Enter part of a movie title: ').lower()
#
# for movie in movies_list:
# 	if user_input in movie.title.lower():
# 		print(movie)
#
# id = input('Enter a movie id: ')

# do something with id, like look up the movie in the movies dictionary and print out the ratings for that movie, then prompt the user for input again if they want to find similar movies, etc.. etc..
