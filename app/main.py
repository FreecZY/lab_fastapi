from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import study, movie, auth

app = FastAPI()

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


app.include_router(study.router)
app.include_router(movie.router)
app.include_router(auth.router)