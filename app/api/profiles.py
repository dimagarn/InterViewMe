from fastapi import APIRouter, HTTPException
from models.profile import InterviewerProfile
from data.mock_data import all_interviewers

router = APIRouter()

@router.get("/profiles/")
def get_all_profiles():
    return all_interviewers

@router.get("/profiles/{profile_id}")
def get_profile_by_id(profile_id: int):
    if profile_id >= len(all_interviewers) or profile_id < 0:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return all_interviewers[profile_id]