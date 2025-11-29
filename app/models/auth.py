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




"""class LoginRequest(BaseModel):
    login: str
    password: str


class LoginResponse(BaseModel):
    token: str
    expires: datetime


class SessionData(BaseModel):
    expires: datetime
    login: str


class JWTPayload(BaseModel):
    login_request: LoginRequest
    exp: int


class UserResponse(BaseModel):
    session_data: SessionData
    user_data: LoginRequest
    movies: list[Movie]"""
