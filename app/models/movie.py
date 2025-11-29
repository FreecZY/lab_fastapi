from pydantic import BaseModel


class Movie(BaseModel):
    name: str
    id: int
    cost: int
    director: str
    is_available: bool = True
    poster: str | None = None