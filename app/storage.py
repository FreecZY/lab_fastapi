# app/storage.py
from app.models.movie import Movie

SECRET = "bgitu_super_secret_key_2025"

MOVIES: list[Movie] = [
    Movie(name="Inception", id=1, cost=160000000, director="Christopher Nolan"),
    Movie(name="The Dark Knight", id=2, cost=185000000, director="Christopher Nolan"),
    Movie(name="Pulp Fiction", id=3, cost=8000000, director="Quentin Tarantino"),
    Movie(name="Forrest Gump", id=4, cost=55000000, director="Robert Zemeckis"),
    Movie(name="The Matrix", id=5, cost=63000000, director="Lana & Lilly Wachowski"),
    Movie(name="Interstellar", id=6, cost=165000000, director="Christopher Nolan"),
    Movie(name="Fight Club", id=7, cost=63000000, director="David Fincher"),
    Movie(name="The Godfather", id=8, cost=6000000, director="Francis Ford Coppola"),
    Movie(name="Parasite", id=9, cost=11400000, director="Bong Joon-ho"),
    Movie(name="Avengers: Endgame", id=10, cost=356000000, director="Russo Brothers"),
]