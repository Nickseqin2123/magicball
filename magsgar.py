import sys
from random import choice


def start(user_nm=None):
    a = ["Бесспорно", "Мне кажется - да", "Пока неясно", "попробуй снова", "Даже не думай",
         "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
         "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
         "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие",
         "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

    if user_nm is None:
        print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.")
        user_name = input("""Как вас зовут ?
        """)
        print(f"Привет {user_name}!")
        if input("""Начнем игру?
            """).lower() == 'да':
            print("Поехали(Вот только куда?)")
            rules(user_name, a)
        else:
            print("Значит начинаем :>(У тебя нет выбоа, здесь я главный)")
            rules(user_name, a)
    else:
        print("Поехали(опять)")
        rules(user_nm, a)


def rules(user_name, spi):
    if input("""Правила помнишь?""") == "нет":
        print("""Итак, объясню правила
        1.Никому не говорить про эту игру
        2.Не упоминать эту игру НИГДЕ
        3.Если нарушил пункт №1, то предлагаю сыграть в русскую рулетку с удалением папки system32
        Приятной игры
        """)

    st = int(input("""Итак, что выберешь?
    1 - Играем в русскую рулетку
    2 - Ты задаешь мне вопрос, а я на него отвечаю
    """))
    if st == 2:
        start_game(user_name, spi)


def start_game(user_name, spi):
    question = input(f"""Какой вопрос задашь мне {user_name}?

    """)
    otv = choice(spi)
    while True:
        if input("""Это все ?
        """).lower() == "да":
            itog(user_name, otv)
            break
        else:
            input("""Задавай
            """)
            new_otv = choice(spi)
            if otv == new_otv:
                new_otv = choice(spi)
                itog(user_name, otv, new_otv)
                break


def itog(user_name, on_otv, two_otv=None):
    if two_otv is None:
        print(f"""{user_name}, вот ответ на твой вопрос:
        {on_otv}""")
    else:
        print(f"""{user_name}, вот ответы на твои вопросы:
        1.{on_otv}
        2.{two_otv}
        """)

    if input("""Сыграем еще ?
    """).lower() == "да":
        start(user_name)
    else:
        print("Пока-пока")
        sys.exit()


if __name__ == "__main__":
    start()
