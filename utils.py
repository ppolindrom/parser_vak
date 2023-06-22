from hh import HHJobPlatform
from superjob import SuperJobPlatform
from vacancy_class import Vacancy


def hh_func(keyword, count_vacancy):
    """Функция вызова класса для работы с хх ру, выводит вакансии по параметрам"""
    get_list = HHJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.job_dictionary()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий.')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')


def sj_func(keyword, count_vacancy):
    """Функция вызова класса для работы с суперджоб, выводит вакансии по параметрам"""
    get_list = SuperJobPlatform(keyword, count_vacancy)  # Создаем экземпляр класса с параметрами пользователя
    list_job = get_list.job_dictionary()  # Получаем список вакансий из класса
    print(f'Нашлось {len(list_job)} вакансий!')
    Vacancy.all_class_vacancy = []
    Vacancy.class_vacancy_ex(list_job)
    for item in Vacancy.all_class_vacancy:  # Перебираем и выводим список
        print(str(item))
    print('Чтобы посмотреть вакансию полностью, нажми на ссылку, браузер откроется автоматически')
