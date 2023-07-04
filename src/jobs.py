from abc import ABC, abstractmethod
import httpx
import ujson
import os

SUPER_JOB_API = "v3.r.137628441.065b9b8deae7dce637fcff2952f982e386912ba2.e9067c71aa6de6605c3d46f5446f11c25c640834"


class Job(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HH_jobs(Job):
    """
    Класс для получения вакансий от HH по API

    Атрибуты:
        name (str): Имя вакансии

    Методы:
        get_vacancies(): Получает список вакансий в формате json
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.params = {
            'text': 'NAME:' + self.name,  # Поиска вакансии по имени
            'page': 0,  # Страница в HH
            'per_page': 100,  # Количество вакансий на 1 странице
        }

    def get_vacancies(self) -> dict:
        """
        Метод для получения данных по заданной вакансии

        :return: Список вакансий в формате json

        """
        hh_request = httpx.get('https://api.hh.ru/vacancies', params=self.params)
        hh_row_data = hh_request.content.decode()
        hh_json = ujson.loads(hh_row_data)

        return hh_json

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}')"


# hh = HH_jobs("Software Engineer")
# vacancies = hh.get_vacancies()
# print(vacancies)

class Super_Job(Job):
    """
    Класс для получения вакансий от SuperJob по API.

    Атрибуты:
    name (str): Название вакансии

    Методы:
    get_vacancies(): Получает список вакансий в формате JSON

    """
    api: str = os.environ.get("SUPER_JOB_API",
                              "v3.r.137628441.065b9b8deae7dce637fcff2952f982e386912ba2.e9067c71aa6de6605c3d46f5446f11c25c640834")

    headers = {
        "Host": "api.superjob.ru",
        "X-Api-App-Id": api,
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    def __init__(self, name: str) -> None:
        """
        Инициализация объекта Super_Job.

        Параметры:
        name (str): Название вакансии
        """
        self.name = name
        self.params = {
            'keywords': [self.name],  # Название вакансии
            'payment_from': 0,  # зарплата от
            'published': 1,
        }

    def get_vacancies(self) -> dict:
        """
        Получает список вакансий от SuperJob в формате JSON.

        Возвращает:
        dict: Список вакансий в формате JSON
        """
        get_sup = httpx.get('https://api.superjob.ru/2.0/vacancies/',
                            params=self.params,
                            headers=self.headers)
        date_super_job = get_sup.content.decode()
        super_job_ujson = ujson.loads(date_super_job)

        return super_job_ujson

    def __str__(self) -> str:
        """
        Возвращает название вакансии в виде строки.
        """
        return self.name

    def __repr__(self) -> str:
        """
        Возвращает название вакансии в виде строки.
        """
        return f"{self.__class__.__name__}('{self.name}')"

# sj = Super_Job("Java")
# vacancies = sj.get_vacancies()
# print(vacancies)
