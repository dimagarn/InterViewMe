from fastapi import APIRouter, HTTPException
from models.profile import InterviewerProfile
from data.mock_data import all_interviewers
import random

router = APIRouter()

def _get_profile_by_id(profile_id: int) -> InterviewerProfile:
    if profile_id >= len(all_interviewers) or profile_id < 0:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return all_interviewers[profile_id]

def _get_random_index(items: list, error_message: str) -> int:
    if len(items) == 0:
        raise HTTPException(status_code=404, detail=error_message)

    random_index = random.choice(range(len(items)))
    return random_index


@router.get("/profiles/")
def get_all_profiles():
    return all_interviewers

@router.get("/profiles/{profile_id}")
def get_profile_by_id(profile_id: int):
    return _get_profile_by_id(profile_id)

@router.get("/profiles/{profile_id}/random_phrase")
def get_random_phrase(profile_id: int):
    profile = _get_profile_by_id(profile_id)
    phrase_index = _get_random_index(profile.typical_phrases, "У данного профиля нет фраз")

    phrase_info = {
        "text": profile.typical_phrases[phrase_index],
        "profile_id": profile_id,
        "profile_title": profile.title,
        "phrase_index": phrase_index
    }
    return phrase_info

@router.get("/profiles/{profile_id}/random_advice")
def get_random_advice(profile_id: int):
    profile = _get_profile_by_id(profile_id)
    advice_index = _get_random_index(profile.advice_tips, "У данного профиля нет советов")

    advice_info = {
        "text": profile.advice_tips[advice_index],
        "profile_id": profile_id,
        "profile_title": profile.title,
        "advice_index": advice_index
    }
    return advice_info

@router.get("/profiles/{profile_id}/random_revenge")
def get_random_revenge(profile_id: int):
    profile = _get_profile_by_id(profile_id)
    revenge_index = _get_random_index(profile.revenge_tactics, "У данного профиля нет тактик мести")

    revenge_info = {
        "text": profile.revenge_tactics[revenge_index],
        "profile_id": profile_id,
        "profile_title": profile.title,
        "revenge_index": revenge_index
    }
    return revenge_info