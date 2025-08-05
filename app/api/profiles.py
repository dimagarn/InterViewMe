from fastapi import APIRouter, HTTPException
from models.profile import InterviewerProfile
from data.mock_data import all_interviewers
from schemas.responses import RandomPhraseResponse, RandomAdviceResponse, RandomRevengeResponse, ProfileListResponse
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


@router.get("/profiles/", response_model=ProfileListResponse)
def get_all_profiles():
    """
    Получить список всех профилей собеседующих

    Возвращает полный список доступных типов собеседующих с их характеристиками
    и особенностями.

    :return: Список всех профилей собеседующих
    :rtype: ProfileListResponse
    """

    response = ProfileListResponse(
        profiles = all_interviewers,
        count = len(all_interviewers)
    )

    return response


@router.get("/profiles/{profile_id}", response_model=InterviewerProfile)
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


@router.get("/profiles/{profile_id}/random_phrase", response_model=RandomPhraseResponse)
def get_random_phrase(profile_id: int):
    """
    Получить случайную фразу собеседующего

    Возвращает случайную фразу из списка типичных фраз собеседующего по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст фразы, ID профиля, название профиля, порядковый номер фразы, количество фраз
    :rtype: RandomPhraseResponse
    :raises HTTPException: 404 если профиль не найден или у профиля нет фраз
    """
    profile = _get_profile_by_id(profile_id)
    phrase_index = _get_random_index(profile.typical_phrases, "У данного профиля нет фраз")

    response = RandomPhraseResponse(
       text = profile.typical_phrases[phrase_index],
       profile_id = profile_id,
       profile_title = profile.title,
       phrase_index = phrase_index,
       count = len(profile.typical_phrases)
    )
    return response


@router.get("/profiles/{profile_id}/random_advice", response_model=RandomAdviceResponse)
def get_random_advice(profile_id: int):
    """
    Получить случайный совет для общения с собеседующим

    Возвращает случайный совет из списка рекомендаций по общению с собеседующим по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст совета, ID профиля, название профиля, порядковый номер совета, количество советов
    :rtype: RandomAdviceResponse
    :raises HTTPException: 404 если профиль не найден или у профиля нет советов
    """
    profile = _get_profile_by_id(profile_id)
    advice_index = _get_random_index(profile.advice_tips, "У данного профиля нет советов")

    response = RandomAdviceResponse(
        text = profile.advice_tips[advice_index],
        profile_id = profile_id,
        profile_title = profile.title,
        advice_index = advice_index,
        count=len(profile.advice_tips)
    )
    return response


@router.get("/profiles/{profile_id}/random_revenge", response_model=RandomRevengeResponse)
def get_random_revenge(profile_id: int):
    """
    Получить случайную тактику мести против собеседующего

    Возвращает случайную юмористическую тактику мести против собеседующего по его ID.

    :param profile_id: ID профиля (0=Душнила, 1=Раздувной, 2=Чилл-гай, 3=Паникёр)
    :type profile_id: int
    :return: Объект содержащий текст тактики мести, ID профиля, название профиля, порядковый номер тактики, количество тактик
    :rtype: RandomRevengeResponse
    :raises HTTPException: 404 если профиль не найден или у профиля нет тактик мести
    """
    profile = _get_profile_by_id(profile_id)
    revenge_index = _get_random_index(profile.revenge_tactics, "У данного профиля нет тактик мести")

    response = RandomRevengeResponse(
        text = profile.revenge_tactics[revenge_index],
        profile_id = profile_id,
        profile_title = profile.title,
        revenge_index = revenge_index,
        count=len(profile.revenge_tactics)
    )
    return response
