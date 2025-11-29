import jwt
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Response, Request, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.models.auth import JWTPayload, UserResponse
from app.storage import MOVIES, SECRET
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/auth", tags=["auth"])
TEMPLATES = Jinja2Templates(directory="app/templates")

@router.get("/login")
async def login_page(request: Request):
    return TEMPLATES.TemplateResponse("login_cookie.html", {"request": request})

SESSIONS = {}

# Авторизация через cookie
@router.post("/login")
async def login_cookie(
    response: Response,
    login: str = Form(...),      # ← Form(...)
    password: str = Form(...),   # ← Form(...)
):
    if login != "admin" or password != "123":
        raise HTTPException(401, "Invalid credentials")
    
    session_id = f"sess_{hash(login + str(datetime.now()))}"
    expires_at = datetime.now() + timedelta(minutes=2)
    
    SESSIONS[session_id] = {
        "login": login,
        "login_time": datetime.now(),
        "expires_at": expires_at
    }
    
    response.set_cookie(
        key="session_token",
        value=session_id,
        httponly=True,
        max_age=120,
        path="/"
    )
    return {"message": "Logged in via cookie"}

@router.get("/user")
async def user_profile(request: Request):
    token = request.cookies.get("session_token")
    if not token or token not in SESSIONS:
        return JSONResponse({"message": "Unauthorized"}, status_code=401)
    
    session = SESSIONS[token]
    if datetime.now() > session["expires_at"]:
        del SESSIONS[token]
        return JSONResponse({"message": "Unauthorized"}, status_code=401)
    
    # Продлеваем сессию
    session["expires_at"] = datetime.now() + timedelta(minutes=2)
    
    return UserResponse(
        login=session["login"],
        login_time=session["login_time"],
        movies=MOVIES
    )

# Авторизация через JWT
class LoginRequest(BaseModel):
    login: str
    password: str

@router.post("/login/jwt")
async def login_jwt(data: LoginRequest):
    if data.login != "admin" or data.password != "123":
        raise HTTPException(401, "Invalid credentials")
    
    expire = datetime.utcnow() + timedelta(minutes=30)
    token = jwt.encode(
        {"sub": data.login, "exp": expire},
        SECRET,
        algorithm="HS256"
    )
    return {"access_token": token, "token_type": "bearer"}





"""
Invoke-WebRequest -Uri "http://localhost:8165/auth/login/jwt" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"login":"admin","password":"123"}'


  curl.exe -X POST http://localhost:8165/movie/add_with_auth -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc2NDM3ODkwM30.8_xrbDqwRj5EnEAqCiPwO-ZthoVUB0JysAhhVww4lqA" -F "name=Тест JWT" -F "director=Режиссёр" -F "cost=100"
"""