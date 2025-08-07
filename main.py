from fastapi import FastAPI
from routes.auth_routes import router as auth_router

app = FastAPI(title="Login & Registration with GPT Password Strength Check")

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
