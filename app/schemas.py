from pydantic import BaseModel

class AptitudeAnswers(BaseModel):
    answers: dict

class CandidateCreate(BaseModel):
    name: str
    email: str
    phone: str
    password: str

class CandidateLogin(BaseModel):
    email: str
    password: str
    
class CandidateUpdate(BaseModel):
    name: str
    email: str
    phone: str