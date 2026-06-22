from fastapi import FastAPI
from app.routers.resume import router as resume_router
from app.database import engine
from app.routers.job import router as job_router
from app.models import Candidate, Base
from app.routers.aptitude import router as aptitude_router
from app.routers.shortlist import router as shortlist_router
from app.routers.candidate import router as candidate_router
from app.routers.communication import router as communication_router
from app.routers.technical import router as technical_router
from app.routers.hr import router as hr_router
from app.routers.selection import router as selection_router
from app.routers.offer import router as offer_router
from app.routers.joining import router as joining_router




Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Recruitment Platform"
)

app.include_router(candidate_router)
app.include_router(job_router)
app.include_router(resume_router)   # <-- ADD THIS LINE
app.include_router(shortlist_router)
app.include_router(aptitude_router)
app.include_router(technical_router)
app.include_router(communication_router)
app.include_router(hr_router)
app.include_router(selection_router)
app.include_router(offer_router)
app.include_router(joining_router)

@app.get("/")
def home():
    return {
        "message": "AI Recruitment Platform Running Successfully"
    }