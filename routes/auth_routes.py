from fastapi import APIRouter, HTTPException
from models.user_models import UserRegister, UserLogin
from database.mongo import user_collection
from auth.auth_utils import hash_password, verify_password
from auth.gpt_password_checker import is_password_weak

router = APIRouter()

@router.post("/register")
async def register(user: UserRegister):
    if user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered.")

    if await is_password_weak(user.password):
        raise HTTPException(status_code=400, detail="Weak password. Please choose a stronger one.")

    hashed_pw = hash_password(user.password)
    user_collection.insert_one({"email": user.email, "password": hashed_pw})
    return {"message": "User registered successfully."}


@router.post("/login")
async def login(user: UserLogin):
    existing = user_collection.find_one({"email": user.email})
    if not existing or not verify_password(user.password, existing["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    return {"message": "Login successful"}
