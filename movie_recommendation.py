import random

dataset = {
    "sci-fi": ["Star Wars", "Avatar", "Iron Man", "Guardians of the Galaxy", "Planet of the Apes"],
    "horror": ["Conjuring", "Supernatural", "Nun", "The Ring", "Annabelle"],
    "adventure": ["Jumanji", "Journey to the Center of Earth", "Harry Potter", "Life of Pie", "Do Little"],
    "comedy": ["Jumanji", "Hera Pheri", "Horrible Bosses", "21 Jump Street", "3 Idiots", "Golmaal"],
    "action": ["Matrix", "Shooter", "Geronimo", "Gangs of Wasseypur", "Sholay"]
}

user1 = ["Avatar", "Iron Man", "Conjuring", "Supernatural", "Nun", "Jumanji",
         "Hera Pheri", "21 Jump Street", "Matrix", "Shooter", ]
user2 = ["Guardians of the Galaxy", "Star Wars", "Planet of the Apes", "Supernatural", "Nun", "The Ring",
         "Annabelle", "Horrible Bosses", "21 Jump Street", "Geronimo", "Gangs of Wasseypur", "Sholay", "3 Idiots", "Golmaal"]

# find the fav category of user1
# find the movies from that category that user2 has already watched
# find out those movies from the fav category that user2 has watched but user1 has not and recommend those movies to user1

# StarWars -> sc - fi
# Conjuring -> Horror

keys = list(dataset.keys())
categoryOfWatchedMoviesCount = dict.fromkeys(keys, 0)
person1 = user2
person2 = user1

for movie in person1:
    for category in dataset:
        if movie in dataset[category]:
            categoryOfWatchedMoviesCount[category] += 1
            print(f"{movie} -> {category}")

print(categoryOfWatchedMoviesCount)

# find values fom above created dict
values = list(categoryOfWatchedMoviesCount.values())
maxCount = max(values)
# find index of category having max movies watched
indexOfFavCategory = values.index(maxCount)
# find the name of category based on the index
favCategory = keys[indexOfFavCategory]
print("Fav Category is ", favCategory)

person2WatchedMoviesInFavCategory = []

for movie in person2:
    if movie in dataset[favCategory]:
        # find those movies that user 2 has watched from the fav category of user1
        person2WatchedMoviesInFavCategory.append(movie)

print(person2WatchedMoviesInFavCategory)

person1NotWatchedMoviesInFavCategory = list(
    set(person2WatchedMoviesInFavCategory) - set(person1))  # find movies that user2 has watched but user 1 hasn't and convert the set back into list so that we can extract one movie randomly
print(person1NotWatchedMoviesInFavCategory)

print("Recommend movie is", random.choice(
    person1NotWatchedMoviesInFavCategory))
