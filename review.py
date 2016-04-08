import csv
class Movie:
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title

    def __str__(self):
        return 'Movie ID: ' + str(self.id) + ' Title: ' + str(self.title)

class User:
    def __init__(self, user_id, age, gender, occupation, zip_code):
        self.id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zip_code = zip_code

    def __str__(self):
        return 'ID: ' + str(self.id) + ' Age: ' + str(self.age) + ' Gender: ' + str(self.gender) + ' Occupation: ' + str(self.occupation) + ' Zip Code: ' + str(self.zip_code)

class Rating:
    def __init__(self, user_id, item_id, rating):
        self.user_id = user_id
        self.item_id = item_id
        self.rating = rating

    def __str__(self):
        return 'User ID: ' + str(self.user_id) + ' Item ID: ' + str(self.item_id) + ' Rating: ' + str(self.rating)

movie_objects = []
with open('u.item.csv') as import_item_file: # automatically closes the file when done
    reader = csv.DictReader(import_item_file, fieldnames=['movie_id', 'movie_title'], delimiter='|')
    headers = next(reader)
    for row in reader:
        # print(row['movie_id'], row['title'])
        # print(Movie(row))
        movie_id = row['movie_id']
        title = row['movie_title']
        movie_objects.append(Movie(movie_id, title))
    # first_movie = movie_objects[0]
    # print(first_movie)

# for row['movie_id'] in movie_objects:
#     print('hi')

user_objects = []
with open('u.user.csv') as import_user_file:
    reader = csv.DictReader(import_user_file, fieldnames=['user_id', 'age', 'gender', 'occupation', 'zip_code'], delimiter='|')
    headers = next(reader)
    for row in reader:
        user_id = row['user_id']
        age = row['age']
        gender = row['gender']
        occupation = row['occupation']
        zip_code = row['zip_code']
        user_objects.append(User(user_id, age, gender, occupation, zip_code))
    # first_user = user_objects[0]
    # print(first_user)

rating_objects = []
with open('u.data.csv') as import_rating_file:
    reader = csv.DictReader(import_rating_file, fieldnames=['user_id', 'item_id', 'rating'], delimiter='\t')
    headers = next(reader)
    for row in reader:
        user_id = row['user_id']
        item_id = row['item_id']
        rating = row['rating']
        rating_objects.append(Rating(user_id, item_id, rating))
    first_rating = rating_objects[0]
    print(first_rating)
