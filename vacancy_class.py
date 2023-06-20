class Vacancy:
    """Класс создающий экземпляры класса вакансий"""
    all_class_vacancy = []  # список экземпляров класса, изначально пустой

    def __init__(self, id_vac, title, link, salary_min, salary_max, description):
        self.id = id_vac
        self.title = title
        self.link = link
        self.description = description
        self.salary_min = salary_min
        self.salary_max = salary_max

        Vacancy.all_class_vacancy.append(self)

    def __gt__(self, other):
        return int(self.salary_min) > int(other.salary_min)

    def __ge__(self, other):
        return int(self.salary_min) >= int(other.salary_min)

    def __lt__(self, other):
        return int(self.salary_min) < int(other.salary_min)

    def __le__(self, other):
        return int(self.salary_min) <= int(other.salary_min)

    def __eq__(self, other):
        return int(self.salary_min) == int(other.salary_min)

    def __str__(self):
        return f"id: {self.id}\n" \
               f"Заголовок вакансии: {self.title}\n" \
               f"Ссылка на вакансию: {self.link}\n" \
               f"Зарплата от {self.salary_min} до {self.salary_max}\n" \
               f"Описание вакансии: {self.description}\n"

    @classmethod
    def class_vacancy_ex(cls, reader):
        """Метод для создания экземпляров класса"""
        for row in reader:
            cls(row['id'], row['title'], row['link'], row['salary_min'], row['salary_max'], row['description'])