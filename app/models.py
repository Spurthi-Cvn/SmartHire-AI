from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base


# =====================================
# CANDIDATE MODEL
# =====================================

class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    phone = Column(String, nullable=False)

    password = Column(String, nullable=False)


# =====================================
# RESUME MODEL
# =====================================

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


# =====================================
# APTITUDE RESULT MODEL
# =====================================

class AptitudeResult(Base):

    __tablename__ = "aptitude_results"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False
    )

    score = Column(Integer, nullable=False)

    percentage = Column(String, nullable=False)

    status = Column(String, nullable=False)

    answers = Column(Text, nullable=True)
    # =====================================
# RECRUITMENT PROGRESS MODEL
# =====================================

class RecruitmentProgress(Base):

    __tablename__ = "recruitment_progress"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        unique=True,
        nullable=False
    )

    current_stage = Column(
        String,
        default="resume"
    )

    ats_status = Column(
        String,
        default="Pending"
    )

    aptitude_status = Column(
        String,
        default="Pending"
    )

    technical_status = Column(
        String,
        default="Locked"
    )

    communication_status = Column(
        String,
        default="Locked"
    )

    hr_status = Column(
        String,
        default="Locked"
    )

    selection_status = Column(
        String,
        default="Pending"
    )

    offer_status = Column(
        String,
        default="Locked"
    )

    onboarding_status = Column(
        String,
        default="Locked"
    )