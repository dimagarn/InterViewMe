from pydantic import BaseModel

class InterviewerProfile(BaseModel):
    title: str
    description: str
    typical_phrases: list[str]
    advice_tips: list[str]
    avatar_url: str
    revenge_tactics: list[str]