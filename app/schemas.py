from pydantic import BaseModel
from pydantic import BaseModel, Field
from typing import Dict

from typing import Dict

from typing import Dict

class HRAnswers(BaseModel):
    answers: Dict[str, str]

class TechnicalAnswers(BaseModel):
    answers: Dict[str, str]
    
class CommunicationAnswers(BaseModel):
    answers: dict

class AptitudeAnswers(BaseModel):
    candidate_id: int
    answers: Dict[str, str] = Field(..., min_length=1)

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