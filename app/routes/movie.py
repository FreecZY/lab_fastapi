import os
import time
from fastapi import APIRouter, File, Form, UploadFile, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from app.models.movie import Movie
from app.models.auth import JWTPayload  # ← ПРАВИЛЬНЫЙ ИМПОРТ
from app.storage import SECRET, MOVIES

router = APIRouter(prefix="/movie", tags=["movie"])


from fastapi.templating import Jinja2Templates
TEMPLATES = Jinja2Templates(directory="app/templates")

@router.get("/add", response_class=HTMLResponse)
async def add_movie_form(request: Request):
    return TEMPLATES.TemplateResponse("add_movie.html", {"request": request})

@router.get("/top")
async def get_top_movies() -> list[Movie]:
    return MOVIES

@router.get("/json/{movie_id}")
async def get_movie_json(movie_id: int) -> Movie:
    for m in MOVIES:
        if m.id == movie_id:
            return m
    raise HTTPException(404, "Film not found")

@router.get("/{movie_id}", response_class=HTMLResponse)
async def get_movie_page(movie_id: int, request: Request):
    movie = await get_movie_json(movie_id)
    return TEMPLATES.TemplateResponse("get_movie.html", {"request": request, "movie": movie})

@router.get("/movietop/{movie_name}")
async def get_movie_by_name(movie_name: str) -> Movie:
    for m in MOVIES:
        if m.name.lower() == movie_name.lower():
            return m
    raise HTTPException(404, "Film not found")

@router.post("")
async def add_movie(
    poster: UploadFile = File(None),
    description_file: UploadFile = File(None),
    name: str = Form(...),
    director: str = Form(...),
    cost: int = Form(...),
    is_available: bool = Form(True),
):
    os.makedirs("uploads", exist_ok=True)

    if description_file:
        safe_name = "".join(c for c in description_file.filename if c.isalnum() or c in "._- ")
        desc_filename = f"desc_{int(time.time())}_{safe_name}"
        with open(f"uploads/{desc_filename}", "wb") as f:
            f.write(await description_file.read())
    
    poster_name = None
    if poster:
        poster_name = f"{int(time.time())}_{poster.filename}"
        with open(f"uploads/{poster_name}", "wb") as f:
            f.write(await poster.read())

    new_id = max(m.id for m in MOVIES) + 1 if MOVIES else 1
    new_movie = Movie(
        name=name,
        id=new_id,
        cost=cost,
        director=director,
        is_available=is_available,
        poster=poster_name
    )
    MOVIES.append(new_movie)
    return {"message": "Film added successfully", "id": new_id}

security = HTTPBearer()

async def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")

@router.post("/add_with_auth")
async def add_movie_auth(
    poster: UploadFile = File(None),
    description_file: UploadFile = File(None),
    name: str = Form(...),
    director: str = Form(...),
    cost: int = Form(...),
    is_available: bool = Form(True),
    user: str = Depends(verify_token)
):
    os.makedirs("uploads", exist_ok=True)

    if description_file:
        safe_name = "".join(c for c in description_file.filename if c.isalnum() or c in "._- ")
        desc_filename = f"desc_{int(time.time())}_{safe_name}"
        with open(f"uploads/{desc_filename}", "wb") as f:
            f.write(await description_file.read())

    poster_name = None
    if poster:
        poster_name = f"{int(time.time())}_{poster.filename}"
        with open(f"uploads/{poster_name}", "wb") as f:
            f.write(await poster.read())

    new_id = max(m.id for m in MOVIES) + 1 if MOVIES else 1
    new_movie = Movie(
        name=name,
        id=new_id,
        cost=cost,
        director=director,
        is_available=is_available,
        poster=poster_name
    )
    MOVIES.append(new_movie)
    return {"message": f"Film added by {user}", "id": new_id}