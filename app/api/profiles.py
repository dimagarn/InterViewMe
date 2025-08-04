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
    """
    Получить список всех профилей собеседующих

    Возвращает полный список доступных типов собеседующих с их характеристиками
    и особенностями.

    :return: Список всех профилей собеседующих
    :rtype: list
    """
    return all_interviewers

@router.get("/profiles/{profile_id}")
def get_profile_by_id(profile_id: int):
    """
    Получить профиль собеседующего по ID

    Возвращает полную информацию о конкретном профиле собеседующего по ID,
    включая его фразы, советы по общению и тактики мести.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект с полной информацией о профиле
    :rtype: InterviewerProfile
    :raises HTTPException: 404 если профиль не найден
    """
    return _get_profile_by_id(profile_id)

@router.get("/profiles/{profile_id}/random_phrase")
def get_random_phrase(profile_id: int):
    """
    Получить случайную фразу собеседующего

    Возвращает случайную фразу из списка типичных фраз собеседующего по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст фразы, ID профиля, название профиля, порядковый номер фразы
    :rtype: dict
    :raises HTTPException: 404 если профиль не найден или у профиля нет фраз
    """
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
    """
    Получить случайный совет для общения с собеседующим

    Возвращает случайный совет из списка рекомендаций по общению с собеседующим по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст совета, ID профиля, название профиля, порядковый номер совета
    :rtype: dict
    :raises HTTPException: 404 если профиль не найден или у профиля нет советов
    """
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
    """
    Получить случайную тактику мести против собеседующего

    Возвращает случайную юмористическую тактику мести против собеседующего по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст тактики мести, ID профиля, название профиля, порядковый номер тактики
    :rtype: dict
    :raises HTTPException: 404 если профиль не найден или у профиля нет тактик мести
    """
    profile = _get_profile_by_id(profile_id)
    revenge_index = _get_random_index(profile.revenge_tactics, "У данного профиля нет тактик мести")

    revenge_info = {
        "text": profile.revenge_tactics[revenge_index],
        "profile_id": profile_id,
        "profile_title": profile.title,
        "revenge_index": revenge_index
    }
    return revenge_info