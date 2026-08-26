from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base


class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String, nullable=False)

    password = Column(String, nullable=False)


class Resume(Base):

    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False
    )

    filename = Column(String, nullable=False)

    resume_text = Column(Text, nullable=True)

    skills = Column(Text, nullable=True)

    match_percentage = Column(String, nullable=True)