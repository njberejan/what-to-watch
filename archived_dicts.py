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
    def __init__(self, user_id, item_id, rating, timestamp):
        self.id = user_id
        self.item_id = item_id
        self.rating = rating
        self.timestamp = timestamp

    def __str__(self):
        return 'User ID: {}, Item ID: {}, Rating: {}'.format(self.id, self.item_id, self.rating)

    def find_all_ratings_by_userid(self):
    	user_dict = {}
    	user_list = []
    	user_id = input("Please enter a User ID number: ")
    	for objects in ratings:
    		if ratings[rating.timestamp] == user_id:
    			user_list.append(ratings[rating.rating])
    		user_dict[user_id] = user_list
    	all_user_ratings = user_dict
    	return all_user_ratings

    # def find_all_ratings_by_movieid(self):
    # 	ratings_dict = {}
    # 	ratings_list = []
    # 	requested_movie = input("Please enter a Movie ID number: ")
    # 	for lists in ratings_data_list:
    # 		for index in lists:
    # 			if lists[1] == requested_movie:
    # 				ratings_list.append(int(lists[2]))
    # 		ratings_dict[requested_movie] = ratings_list
    # 	all_ratings_by_movieid = ratings_dict
    # 	return all_ratings_by_movieid, requested_movie, ratings_dict
    #
    # def find_average_rating_by_movieid(all_ratings_by_movieid, requested_movie):
    #     average_rating_by_movieid = sum(all_ratings_by_movieid[requested_movie]) / len(all_ratings_by_movieid[requested_movie])
    #     print(average_rating_by_movieid)
    #
    # def display_top_movies(all_ratings_by_movieid, requested_movie, ratings_dict):
    # 	movie_average_dict = {}
    # 	for key in ratings_dict:
    # 		if len(all_ratings_by_movieid[requested_movie]) > 5:
    # 			movie_average_dict[movie_id] = find_average_rating_by_movieid(all_ratings_by_movieid, requested_movie)
    # 	print(movie_average_dict)

movies = {}
with open('u.item.csv', encoding='latin_1') as item_file:
    reader = csv.DictReader(item_file, delimiter='|', fieldnames=['movie_id', 'title'])
    for row in reader:
        movie = Movie(row['movie_id'], row['title'])
        movies[movie.id] = movie #creates dict "movies" with the movie ID as the key and the title as the value
    print(movies['1'])
    print(movies['1'].title)

users = {}
with open('u.user.csv', encoding='latin_1') as user_file:
    reader = csv.DictReader(user_file, delimiter='|', fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'])
    for row in reader:
        user = User(row['user_id'], row['age'], row['gender'], row['occupation'], row['zip_code'])
        users[user.id] = user #creates dictionary "users" with user ID as the key and THE OBJECT AS THE VALUE
    print(users['1'])
    print(users['1'].occupation)

ratings = {}
with open('u.data.csv', encoding='latin_1') as ratings_file: #CREATES LIST OF EACH LINE AS A LIST
    reader = csv.DictReader(ratings_file, delimiter='\t', fieldnames=['user_id', 'item_id',	'rating', 'timestamp'])
    for row in reader:
        rating = Rating(row['user_id'], row['item_id'], row['rating'], row['timestamp'])
        ratings[rating.timestamp] = rating
    print(ratings['881250949'])
    print(ratings['881250949'].item_id)


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

# def find_all_ratings_by_movieid(ratings_data_list):
    #movie id number is index 1 in ratings_list
# print(ratings_data_list)

# all_ratings_by_movieid, requested_movie, ratings_dict = find_all_ratings_by_movieid()
# print(all_ratings_by_movieid)
# # #returns dictionary with key as entered value and value a list of all ratings for a movie by movie ID
# find_average_rating_by_movieid(all_ratings_by_movieid, requested_movie)
# # #prints average score for a movie by ID, based on output from find_all_ratings_by_movieid()
# # Movie.movies_listed_by_title(movies)
# # #asks user to input part of a title and returns list of all matches containing part of that title
# # Movie.find_title_by_id(movies)
# # #prints title of movie by ID number provided
# # all_ratings_by_user = find_all_ratings_by_userid()
# # print(all_ratings_by_user)
# display_top_movies(all_ratings_by_movieid, requested_movie, ratings_dict)
all_user_ratings = Rating.find_all_ratings_by_userid(rating)
print(all_user_ratings)