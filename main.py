from utils import hh_func, sj_func


def main():
    """Основная функция для запуска программы"""
    print('Привет! Я могу помочь найти тебе работу.')

    while True:
        while True:
            first_question = input('Где будем искать?\n'
                                   '1 - HH.ру\n'
                                   '2 - SuperJob\n')
            if first_question == '1' or first_question == '2':
                break

            else:
                print('Не правильно ввел. Попробуй еще раз.')
                continue

        while True:
            keyword = input('Что будем искать? Введи ключевое слово (Например: "python", или "java")\n')
            if len(keyword.lower()) <= 2:
                print("Не правильно ввел. Попробуй еще раз.")
                continue
            else:
                break

        while True:
            count_vacancy = input('Сколько ваканcий тебе показать?\n')
            try:
                if int(count_vacancy) > 1:
                    break
                else:
                    print("Нужно указать больше одной вакансии!")
                continue

            except ValueError:
                print("Вы ничего не вводите")
                continue

        while True:
            city = input('В каком городе?\n')
            if len(city.lower()) <= 2:
                print("Не правильно ввел. Попробуй еще раз.")
                continue
            else:
                break

        keyword_end = keyword + ' ' + city  # составляем ключевое слово, запрос

        if first_question == '1':
            hh_func(keyword_end, count_vacancy)

        elif first_question == '2':
            sj_func(keyword_end, count_vacancy)

        while True:
            answer_end = input('Давай поищем что-нибудь еще? Да/Нет\n')
            if answer_end.lower() == 'да' or answer_end.lower() == 'lf':
                break
            elif answer_end.lower() == 'нет' or answer_end.lower() == 'ytn':
                print('Хорошо. До встречи!')
                exit()

            else:
                print('Нужно ответить "да" или "нет"')
                continue


if __name__ == '__main__':
    main()
