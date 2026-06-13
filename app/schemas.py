from pydantic import BaseModel

class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class CandidateLogin(BaseModel):
    email: str
    password: str