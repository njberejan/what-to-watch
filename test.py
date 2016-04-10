import csv
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
#print debugging stuff
print(movie_dict[1].title)
# movie = movie_dict[123]
# print(movie.ratings)
# print(movie.ratings[0])
# print(movie.ratings[0][1])
ratings = []

for movie_id in movie_dict:
	movie = movie_dict[movie_id]
	for rating in movie.ratings:
		ratings.append(rating[1])
print(ratings)


# test_list = []
# for movie_object in movie_dict:
# 	for movie_object.ratings in movie_object:
# 		test_list = test_list.append(objects.ratings[0])
# print(test_list)

# print(movie_ratings_dict)

# all_movies_average_scores = {}
# for key in movie_ratings_dict:
# 	print(type(key))
	# all_movies_average_scores = sum(key[1])
# print(all_Movies_average_scores)



#_______BOUDROUS CODE__________

# import csv
# class Movie:
#     def __init__(self, row, ratings):
#         self.id = int(row['MovieID'])
#         self.title = row['MovieTitle']
#         self.ratings = ratings
#         self.average = self.find_average_rating(ratings)
#         self.number_of_ratings = len(ratings)
# ​
#     def __str__(self):
#         return "{}: {}".format(self.id, self.title)
# ​
#     def __repr__(self):
#         return str(self)
# ​
#     def find_average_rating(self, ratings):
#         total = sum([t[1] for t in ratings])
#         return float("%.2f" % (total / len(ratings)))
#
# def get_movie_dict(movie_ratings_dict):
#     with open('u.item', encoding='latin_1') as f:
#         movie_dict = {}
#         reader = csv.DictReader(f, fieldnames=['MovieID', 'MovieTitle'], delimiter='|')
#         for row in reader:
#             movie_dict[int(row['MovieID'])] = Movie(row, movie_ratings_dict[int(row['MovieID'])])
#     return movie_dict
# ​
# ​
# def get_movie_ratings_dict():
#     with open('u.data', encoding='latin_1') as f:
#         movie_ratings_dict = {}
#         reader = csv.DictReader(f, fieldnames=['UserID', 'MovieID', 'Rating', 'Time'], delimiter='\t')
#         for row in reader:
#             if int(row['MovieID']) in movie_ratings_dict:
#                 movie_ratings_dict[int(row['MovieID'])].append((int(row['UserID']), int(row['Rating'])))
#             else:
#                 movie_ratings_dict[int(row['MovieID'])] = [(int(row['UserID']), int(row['Rating']))]
#     return movie_ratings_dict
