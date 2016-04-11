import csv
import operator
from movie import Movie
from user import User

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

#attempt to get 95th percentile of average scores in dict. How to get add second values in tuple without pulling into second list?
sorted_averages = sorted(all_average_scores_dict.items(), key=operator.itemgetter(1))
print(sorted_averages)
sorted_values = []
for value1, value2 in sorted_averages:
	sorted_values.append(value2)
print(sorted_values)
import numpy as np #attempt to import numpy to get 95 percentile below
print(np.percentile(sorted_values, 95))
