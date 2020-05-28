dataset = {
    "sci-fi": ["Star Wars", "Avatar", "Iron Man", "Guardians of the Galaxy", "Planet of the Apes"],
    "horror": ["Conjuring", "Supernatural", "Nun", "The Ring", "Annabelle"],
    "adventure": ["Jumanji", "Journey to the Center of Earth", "Harry Potter", "Life of Pie", "Do Little"],
    "comedy": ["Hera Pheri", "Horrible Bosses", "21 Jump Street", "3 Idiots", "Golmaal"],
    "action": ["Matrix", "Shooter", "Geronimo", "Gangs of Wasseypur", "Sholay"]
}

user1 = ["Star Wars", "Avatar", "Iron Man", "Conjuring", "Supernatural", "Jumanji",
         "Hera Pheri", "Horrible Bosses", "21 Jump Street""Matrix", "Shooter", ]
user2 = ["Guardians of the Galaxy", "Planet of the Apes", "Supernatural", "Nun", "The Ring",
         "Horrible Bosses", "21 Jump Street", "Geronimo", "Gangs of Wasseypur", "Sholay"]

# find the fav category of user1
# find the movies from that category that user2 has already watched
# find out those movies from the fav category that user2 has watched but user1 has not and recommend those movies to user1

# StarWars -> sc - fi
# Conjuring -> Horror
