import csv
class Movie:
	def __init__(self, movie_id, title):
		self.id = row['movie_id']
		self.title = row['title']


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

# class Rating:
#
#     def __init__(self, row):
#         self.id = row[0]
#         self.item_id = row[1]
#         self.rating = row[2]
#
#     def __str__(self):
#         return 'User ID: {}, Item ID: {}, Rating: {}'.format(self.id, self.item_id, self.rating)
#
#     def find_all_ratings_by_userid(ratings_data_list):
#         #returns dictionary with key User ID and value list of all reviews from user
#         user_dict = {}
#         user_list = []
#         user_id = input("Please enter a User ID number: ")
#         for objects in ratings_data_list:
#             if objects.id == user_id:
#                 user_list.append(objects.rating)
#         user_dict[user_id] = user_list
#         all_user_ratings = user_dict
#         return all_user_ratings
#
#     def find_all_ratings_by_movieid(ratings_data_list):
#         #returns dictionary with key Movie ID and value list of all reviews for movie
#         ratings_dict = {}
#         ratings_list = []
#         movie_id = input("Please enter a Movie ID number: ")
#         for objects in ratings_data_list:
#             if objects.item_id == movie_id:
#                 ratings_list.append(int(objects.rating))
#             ratings_dict[movie_id] = ratings_list
#         all_ratings_by_movieid = ratings_dict
#         return all_ratings_by_movieid, movie_id, ratings_list
#
#     def find_average_rating_by_movieid(ratings_list):
#         #returns average rating for movie by movie ID. Must first run find_all_ratings_by_movieid, however.
#         average_rating_by_movieid = sum(ratings_list) / int(len(ratings_list))
#         return average_rating_by_movieid
#
#     def find_all_ratings_for_all_movies(ratings_data_list):
#         #freezes command line. Theoretically returns dictionary with movie ID as key and list of all ratings as value for every movie
#         all_ratings_dict = {}
#         all_ratings_list = []
#         for objects in ratings_data_list:
#             for objects.item_id in ratings_data_list:
#                 all_ratings_list.append(int(objects.rating))
#         all_ratings_dict[Rating.item_id] = all_ratings_list
#         return all_ratings_dict, all_ratings_list
#
#     def gets_average_rating_for_all_movies(all_ratings_dict):
#         all_average_ratings = {}
#         for objects.item_id in all_ratings_dict:
#             all_average_ratings[objects.item_id] = (sum(all_ratings_dict[objects.item_id]) / len(all_ratings_dict[objects.item_id]))
#         return all_average_ratings

    # def gets_top_movies(ratings_data_list, ratings_list):
    #     top_movies = []
    #     for objects in ratings_data_list:
    #         if objects.find_average_rating_by_movieid(ratings_list) > 3:
    #             top_movies.append(objects.item_id, objects.find_average_rating_by_movid(ratings_list))
    #     return top_movies


    # def get_top_movies(find_average_rating_by_movieid, ratings_data_list):
    #     for objects in ratings_data_list:
    #         if find_average_rating_by_movieid(ratings_list)

users = {}
with open('u.user.csv', encoding='latin_1') as user_file:
    reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    for row in reader:
        user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
        users[user.id] = user #creates dictionary "users" with user ID as the key and THE OBJECT AS THE VALUE
    # print(users['1'])
    # print(users['1'].occupation)

movie_ratings_dict = {}
with open('u.data.csv', encoding='latin_1') as ratings_file:
	reader = csv.DictReader(ratings_file, delimiter='\t', fieldnames=['user_id', 'movie_id', 'rating', 'timestamp'])
	for row in reader:
		if row['movie_id'] in movie_ratings_dict:
			movie_ratings_dict[row['movie_id']].append((row['user_id'], row['rating']))
		else:
			movie_ratings_dict[row['movie_id']] = [(row['user_id'], row['rating'])]
			#imports file and returns dictionary with item id as the key and a list of user id and corresponding review score tuples.

with open('u.item.csv', encoding='latin_1') as item_file:
	movie_dict = {}
	reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
	for row in reader:
		movie_dict[row['movie_id']] = Movie(row['movie_id'], row['title'])
    #creates dict "movies" with the movie ID as the key and the title as the value
    # print(movie)

print(movie_ratings_dict['1'])




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
