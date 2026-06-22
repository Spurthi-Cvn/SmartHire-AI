from fastapi import APIRouter

router = APIRouter()


@router.get("/selection")
def final_selection():

    return {
        "status": "Congratulations",
        "result": "Selected",
        "next_step": "Offer Letter Generation"
    }