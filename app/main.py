from fastapi import FastAPI

from app.database import engine
from app.models import Candidate, Base
from app.routers.candidate import router as candidate_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Recruitment Platform"
)

app.include_router(candidate_router)

@app.get("/")
def home():
    return {
        "message": "AI Recruitment Platform Running Successfully"
    }