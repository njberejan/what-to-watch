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
