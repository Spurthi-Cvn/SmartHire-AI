from fastapi import APIRouter

router = APIRouter()


@router.get("/communication")
def communication_test():

    questions = [
        {
            "id": 1,
            "question": "Choose the correct sentence.",
            "options": [
                "She go to office daily.",
                "She goes to office daily.",
                "She going to office daily.",
                "She gone to office daily."
            ]
        },
        {
            "id": 2,
            "question": "What is the synonym of 'Reliable'?",
            "options": [
                "Trustworthy",
                "Weak",
                "Slow",
                "Lazy"
            ]
        },
        {
            "id": 3,
            "question": "Choose the correct email greeting.",
            "options": [
                "Hey Dude",
                "Dear Hiring Manager",
                "Yo",
                "What's Up"
            ]
        }
    ]

    return {
        "test_name": "Communication Round",
        "questions": questions
    }
    
from fastapi import APIRouter
from app.schemas import CommunicationAnswers

router = APIRouter()


@router.get("/communication")
def communication_test():

    questions = [
        {
            "id": 1,
            "question": "Choose the correct sentence.",
            "options": [
                "She go to office daily.",
                "She goes to office daily.",
                "She going to office daily.",
                "She gone to office daily."
            ]
        },
        {
            "id": 2,
            "question": "What is the synonym of 'Reliable'?",
            "options": [
                "Trustworthy",
                "Weak",
                "Slow",
                "Lazy"
            ]
        },
        {
            "id": 3,
            "question": "Choose the correct email greeting.",
            "options": [
                "Hey Dude",
                "Dear Hiring Manager",
                "Yo",
                "What's Up"
            ]
        }
    ]

    return {
        "test_name": "Communication Round",
        "questions": questions
    }


@router.post("/communication/submit")
def submit_communication(test: CommunicationAnswers):

    correct_answers = {
        "1": "She goes to office daily.",
        "2": "Trustworthy",
        "3": "Dear Hiring Manager"
    }

    score = 0

    for question_id, answer in test.answers.items():
        if correct_answers.get(question_id) == answer:
            score += 1

    percentage = round(
        (score / len(correct_answers)) * 100,
        2
    )

    status = "Passed" if percentage >= 60 else "Failed"

    return {
        "score": score,
        "percentage": percentage,
        "status": status
    }
    
