from models.profile import InterviewerProfile

typical_phrases = [
"А какая временная сложность у quicksort в худшем случае?",
"Расскажите разницу между TCP и UDP протоколами",
"Что происходит при выполнении команды git merge --no-ff?",
"Объясните принцип работы garbage collector в Python",
"А почему вы не использовали паттерн Singleton в этом случае?"
]

advice_tips = [
"Переводите всё в практические примеры - 'Это как пицца...'",
"Начинайте с фразы 'В реальных проектах обычно...'",
"Признайтесь честно: 'Хороший вопрос, а как вы это решаете?'"
]

revenge_tactics = [
"Спросите его про soft skills и эмоциональный интеллект",
"Попросите объяснить код без технических терминов",
"Задайте вопрос: 'А как это поможет бизнесу?'"
]

avatar_url = "https://a.d-cd.net/9aec42as-960.jpg"

nerd_interviewer = InterviewerProfile(
    name = "fred",
    archetype = "душнила",
    description = "классический душнила, постоянно душит своими ненужными советами",
    typical_phrases = typical_phrases,
    advice_tips = advice_tips,
    avatar_url = avatar_url,
    revenge_tactics = revenge_tactics
)

if __name__ == "__main__":
    print("Тестируем модель...")
    print(f"Имя: {nerd_interviewer.name}")
    print(f"Тип: {nerd_interviewer.archetype}")
    print(f"Количество фраз: {len(nerd_interviewer.typical_phrases)}")
    print("Первая фраза:", nerd_interviewer.typical_phrases[0])