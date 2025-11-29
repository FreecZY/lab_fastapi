from datetime import datetime
from pydantic import BaseModel

from app.models.movie import Movie


class JWTPayload(BaseModel):
    sub: str  # login
    exp: int

class UserResponse(BaseModel):
    login: str
    login_time: datetime
    movies: list[Movie]