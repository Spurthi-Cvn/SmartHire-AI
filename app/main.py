from fastapi import FastAPI
from app.routers.resume import router as resume_router
from app.database import engine
from app.routers.job import router as job_router
from app.models import Candidate, Base
from app.routers.shortlist import router as shortlist_router
from app.routers.candidate import router as candidate_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Recruitment Platform"
)

app.include_router(candidate_router)
app.include_router(job_router)
app.include_router(resume_router)   # <-- ADD THIS LINE
app.include_router(shortlist_router)

@app.get("/")
def home():
    return {
        "message": "AI Recruitment Platform Running Successfully"
    }