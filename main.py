from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = [
    {"id": 1, "title": "Harry Potter and the Sorcerer's Stone", "director": "Chris Columbus", "release_year": 2001},
    {"id": 2, "title": "The Lord of the Rings: The Fellowship of the Ring", "director": "Peter Jackson", "release_year": 2001},
    {"id": 3, "title": "Toy Story", "director": "John Lasseter", "release_year": 1995}
]

class Movies(BaseModel):
    title: str
    director: str
    release_year: int

@app.get("/movies")
def get_movies():
    """Get all movies"""
    return {"movies": movies}

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    """Get a specific movie by ID."""
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return {"error": "Movie not found"}