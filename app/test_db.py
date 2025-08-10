from database import SessionLocal
from models.db_models import Profile

db = SessionLocal()
profiles = db.query(Profile).all()

for profile in profiles:
    print(f"ID: {profile.id}, Title: {profile.title}")
    print(f"Фраз: {len(profile.typical_phrases)}")
    print("---")

db.close()