from database import SessionLocal
from models.db_models import Profile
from data.mock_data import all_interviewers

def seed_database():
    """
    Заполняет БД профилями интервьюеров.

    Данные берутся из app/data/mock_data.py для переиспользования
    в тестах и демо-режиме.
    """
    db = SessionLocal()

    try:
        existing_count = db.query(Profile).count()
        if existing_count > 0:
            print(f"В базе уже есть {existing_count} записей. Пропускаем заполнение.")
            return

        print("Начинаем заполнение базы данных...")

        for mock_profile in all_interviewers:
            db_profile = Profile(
                title=mock_profile.title,
                description=mock_profile.description,
                typical_phrases=mock_profile.typical_phrases,
                advice_tips=mock_profile.advice_tips,
                revenge_tactics=mock_profile.advice_tips,
                avatar_url=mock_profile.avatar_url
            )
            db.add(db_profile)
            print(f"Добавлен профиль: {mock_profile.title}")

            db.commit()
            print("База данных успешно заполнена")

            total_count = db.query(Profile).count()
            print(f"Всего записей в БД: {total_count}")

    except Exception as e:
        print(f"Ошибка при заполнении БД: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()