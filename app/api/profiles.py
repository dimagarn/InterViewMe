from fastapi import APIRouter
from models.profile import InterviewerProfile
from data.mock_data import nerd_interviewer
router = APIRouter()

@router.get("/profiles/1")
def get_profile():
    return nerd_interviewer