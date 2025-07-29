from pydantic import BaseModel
from typing import List

class InterviewerProfile(BaseModel):
    title: str
    description: str
    typical_phrases: List[str]
    advice_tips: List[str]
    avatar_url: str
    revenge_tactics: List[str]