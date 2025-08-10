from pydantic import BaseModel

class RandomItemResponse(BaseModel):
    text: str
    profile_id: int
    profile_title: str
    index: int
    count: int

class ProfileListResponse(BaseModel):
    profiles: list
    count: int
