from dataclasses import field

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from models.db_models import Profile
from schemas.responses import RandomItemResponse, ProfileListResponse
from database import get_db
import random
from functools import wraps


router = APIRouter()


def _get_profile_by_id(db: Session, profile_id: int) -> Profile:
    """Получить профиль по ID с проверкой существования"""
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return profile

def random_item_endpoint(field_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(profile_id: int, db: Session = Depends(get_db)):
            profile = _get_profile_by_id(db, profile_id)
            items = getattr(profile, field_name)

            if not items:
                readable_field = field_name.replace("_", " ")
                error_msg = f"Profile has no {readable_field}"
                raise HTTPException(status_code=404, detail=error_msg)
            index = random.randint(0, len(items) - 1)

            return RandomItemResponse(
                text=items[index],
                profile_id=profile.id,
                profile_title=profile.title,
                index=index,
                count=len(items)
            )
        return wrapper
    return decorator

def _get_random_index(items: list, error_message: str) -> int:
    """Получить случайный индекс из списка с проверкой на пустоту"""
    if not items or len(items) == 0:
        raise HTTPException(status_code=404, detail=error_message)
    return random.randint(0, len(items) - 1)

@router.get("/profiles/", response_model=ProfileListResponse)
def get_all_profiles(db: Session = Depends(get_db)):
    """
    Получить список всех профилей собеседующих

    Возвращает полный список доступных типов собеседующих с их характеристиками
    и особенностями.

    :return: Список всех профилей собеседующих
    :rtype: ProfileListResponse
    """
    profiles = db.query(Profile).all()

    response = ProfileListResponse(
        profiles = profiles,
        count = len(profiles)
    )
    return response


@router.get("/profiles/{profile_id}")
def get_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    """
    Получить профиль собеседующего по ID

    Возвращает полную информацию о конкретном профиле собеседующего по ID,
    включая его фразы, советы по общению и тактики мести.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект с полной информацией о профиле
    :rtype: Profile
    :raises HTTPException: 404 если профиль не найден
    """
    profile = db.query(Profile).filter(Profile.id == profile_id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return profile


@router.get("/profiles/{profile_id}/random_phrase")
@random_item_endpoint("typical_phrases")
def get_random_phrase(profile_id: int, db: Session = Depends(get_db)):
    """
    Получить случайную фразу собеседующего

    Реализация автоматически предоставляется декоратором @random_item_endpoint.
    Декоратор обрабатывает получение профиля, выбор случайной фразы и формирование ответа.
    """
    pass


@router.get("/profiles/{profile_id}/random_advice")
@random_item_endpoint("advice_tips")
def get_random_advice(profile_id: int, db: Session = Depends(get_db)):
    """
    Получить случайный совет для общения с собеседующим

    Реализация автоматически предоставляется декоратором @random_item_endpoint.
    Декоратор обрабатывает получение профиля, выбор случайного совета и формирование ответа.
    """
    pass


@router.get("/profiles/{profile_id}/random_revenge", response_model=RandomItemResponse)
@random_item_endpoint("revenge_tactics")
def get_random_revenge(profile_id: int, db: Session = Depends(get_db)):
    """
    Получить случайную тактику мести против собеседующего

    Реализация автоматически предоставляется декоратором @random_item_endpoint.
    Декоратор обрабатывает получение профиля, выбор случайной мести и формирование ответа.
    """
    pass