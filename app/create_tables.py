from database import engine, Base
from models.db_models import Profile

def create_tables():
    print("Создаем таблицы в базе данных...")
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы успешно!")

if __name__ == "__main__":
    create_tables()