from pydantic import BaseModel
from models.profile import InterviewerProfile

class BaseRandomResponse(BaseModel):
    text: str
    profile_id: int
    profile_title: str
    count: int

class RandomPhraseResponse(BaseRandomResponse):
    phrase_index: int

class RandomAdviceResponse(BaseRandomResponse):
    advice_index: int

class RandomRevengeResponse(BaseRandomResponse):
    revenge_index: int

class ProfileListResponse(BaseModel):
    profiles: list[InterviewerProfile]
    count: int