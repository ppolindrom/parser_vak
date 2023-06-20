import json
from abc import ABC

import requests
from abstract_class import AbstractJobPlatform


class SuperJobPlatform(AbstractJobPlatform, ABC):

    def __init__(self, keyword):
        self.keyword = keyword
        self.salary_min = None

    def server_connection(self):
        """Подключение к API sj.ru"""
        headers = {
            'Host': 'api.superjob.ru',
            'X-Api-App-Id': 'v3.r.137621073.4b760f4eda8bad2460b645c40f21ad7f8a883a89.68b12c133699de440c85cd6c234250d172225eee',
            'Authorization': 'Bearer r.000000010000001.example.access_token',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        params = {"count": 10, "page": None,
                  "keyword": self.keyword, "archive": False, }
        data = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params)
        return data

    def job_dictionary(self, **kwargs):
        """Создание словаря вакансий"""
        if self.server_connection().status_code == 200:
            data = self.server_connection().json()
            list_job = []
            for item in data['objects']:
                title = item['profession']
                link = item['link']

                if item['payment_from']:
                    salary_min = item['payment_from']
                    salary_max = item['payment_to']

                else:
                    salary_min = None
                    salary_max = None

                description = item['candidat']
                id_vacancy = item['id']

                jobs = {
                    'id': id_vacancy,
                    'title': title,
                    'link': link,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'description': description
                }
                list_job.append(jobs)
            self.file_vacancy(list_job)
            return list_job

    def file_vacancy(self, jobs):
        """Запись словаря в JSON-файл"""
        with open('vacancy_sj.json', 'w', encoding='utf-8') as json_file:
            json.dump(jobs, json_file, sort_keys=False, indent=4, ensure_ascii=False)