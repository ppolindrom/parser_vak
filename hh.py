import json
from abc import ABC
import requests
from abstract_class import AbstractJobPlatform


class HHJobPlatform(AbstractJobPlatform, ABC):

    def __init__(self, keyword, count_vacancy):
        self.count_vacancy = count_vacancy # количество вакансий нужных пользователю
        self.keyword = keyword # тег для поиска вакансии
        self.salary_min = None # минимальная зарплата


    def server_connection(self, params=None):
        """Подключение к API hh.ru"""

        url = 'https://api.hh.ru/vacancies'
        params = {'text': self.keyword,  # тег для поиска вакансий
                  "per_page": 10  # колличество вакансий на странице
                  }
        headers = {
            "User-Agent": "50355527",  # Replace with your User-Agent header
        }

        response = requests.get(url, params=params, headers=headers)

        return response

    def job_dictionary(self, **kwargs):
        """Создание словаря вакансий"""
        if self.server_connection().status_code == 200:
            data = self.server_connection().json()
            list_job = []
            for item in data['items']:
                id_vac = item['id']
                title = item['name']
                link = item['alternate_url']

                if item['salary']:
                    salary_min = item['salary']['from']
                    salary_max = item['salary']['to']

                else:
                    salary_min = None
                    salary_max = None

                description = item['snippet']['requirement'] if item['snippet'] and 'requirement' in item[
                    'snippet'] else None

                jobs = {
                    'id': id_vac,
                    'title': title,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': description
                }
                list_job.append(jobs)
            self.file_vacancy(list_job)
            return list_job

        else:
            print(f"Request failed with status code: {self.server_connection().status_code}")

    def file_vacancy(self, list_jobs):
        """Запись словаря в JSON-файл"""
        with open('vacancy_hh.json', 'w', encoding='utf-8') as f:
            json.dump(list_jobs, f, sort_keys=False, indent=4, ensure_ascii=False)