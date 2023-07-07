from abc import ABC, abstractmethod
import ujson
import os
import csv


class Saver_file(ABC):
    """
        Абстрактный базовый класс для сохранения данных.
    """
    @abstractmethod
    def jobs_adding(self, jobs):
        """
            Абстрактный метод для добавления вакансий.
        """
        pass

    @abstractmethod
    def get_salary(self, salary):
        """
            Абстрактный метод для получения вакансий по зарплате.
        """
        pass

    @abstractmethod
    def get_city(self, citi):
        """
            Абстрактный метод для получения вакансий по городу.
        """
        pass

    @abstractmethod
    def get_experience(self, experience):
        """
            Абстрактный метод для получения вакансий по опыту работы.
        """
        pass

    @abstractmethod
    def jobs_deleting(self, jobs):
        """
            Абстрактный метод для удаления вакансий.
        """
        pass

    @abstractmethod
    def file_cleaning(self):
        """
            Абстрактный метод для очистки файла..
        """
        pass


class Json_Saver(Saver_file):
    file = os.path.join("saver file", 'vacancy.json')

    def jobs_adding(self, jobs: dict) -> None:
        """
            Метод для добавления вакансий в файл JSON.
        """
        if not os.path.exists(self.file):
            with open(self.file, "w", encoding="utf-8") as file:
                file.write("[]")
        with open(self.file, 'r', encoding="utf-8") as file:
            try:
                json_data = ujson.loads(file.read())
            except ValueError:
                json_data = []
        json_data.append(jobs)
        with open(self.file, "w", encoding="utf-8") as file:
            file.write(ujson.dumps(json_data, indent=2,
                                   ensure_ascii=False,
                                   escape_forward_slashes=False))

    def is_consistent_data(self, job: dict) -> bool:
        """
        Проверка, являются ли данные вакансии консистентными
        :param job: словарь с информацией о вакансии
        :return: bool: True, если данные консистентны, иначе False
        """
        # Проверка наличия всех обязательных полей и их типов данных
        if (
                'name' in job
                and 'experience' in job
                and 'city' in job
                and 'url' in job
                and 'address' in job
                and 'salary' in job
                and isinstance(job['name'], str)
                and isinstance(job['experience'], str)
                and isinstance(job['city'], str)
                and isinstance(job['url'], str)
                and isinstance(job['address'], str) or job['address'] is None
                and isinstance(job['salary'], int) or job['salary'] is None
        ):
            return True
        return False

    def get_salary(self, salary: int) -> list:
        """
            Метод для получения вакансий по зарплате.
        """
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item].get('_Vacancy__salary') == salary]

    def get_city(self, city: str) -> list:
        """
            Метод для получения вакансий по городу.
        """
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in
                    range(len(ujson_data)) if ujson_data[item]['city'] == city]

    def get_experience(self, experience):
        """
            Метод для получения вакансий по опыту работы.
        """
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item]['experience'] == experience]

    def jobs_deleting(self, jobs):
        """
            Метод для удаления вакансий.
        """
        try:
            ujson_data = ujson.load(open(self.file))
            ujson_data.remove(jobs)
            with open(self.file, 'w', encoding="utf-8") as file:
                ujson.dump(ujson_data, file,
                           indent=2, ensure_ascii=False,
                           escape_forward_slashes=False)
        except ValueError:
            print('Все вакансии удалены')

    def file_cleaning(self):
        """
            Метод для очистки файла.
        """
        os.remove(self.file)


# class TXT_Saver(Saver_file):
#     file = os.path.join("saver file", 'vacancy.txt')
#
#     def jobs_adding(self, jobs: dict) -> None:
#         """
#         Метод добавление данных в формате json
#         :param jobs: словарь, который добавляется в файл
#         :return: None
#         """
#         # проверка на существование файла
#         if not os.path.exists(self.file):
#             with open(self.file, 'w', encoding='utf-8') as f:
#                 ujson.dump([], f)
#             # добавление в список вакансий
#         with open(self.file, 'r', encoding='utf-8') as f:
#             file = ujson.load(f)
#             file.append(jobs)
#             # запись в файл
#         with open(self.file, 'w', encoding='utf-8') as f:
#             ujson.dump(file, f)
#
#     def get_salary(self, salary: int) -> list:
#         """
#         Метод на проверку зарплаты
#         :param salary: запралата
#         :return: Список подходящих вакансий
#         """
#         with open(self.file, 'rb') as f:
#             txt_date = ujson.load(f, encoding='utf-8')
#             return [item for item in txt_date if int(item['_Vacancy__salary']) == salary]
#
#     def get_city(self, city: str) -> list:
#         """
#         Метод на проверку города
#         :param city: город
#         :return: Список подходящих вакансий
#         """
#         with open(self.file, 'rb') as f:
#             txt_date = ujson.load(f, encoding='utf-8')
#             return [item for item in txt_date if item['_Vacancy__city'] == city]
#
#     def get_experience(self, experience: str) -> list:
#         """
#         Метод на проверку опыта работы
#         :param experience: опыт работы
#         :return: Список подходящих вакансий
#         """
#         with open(self.file, 'rb') as f:
#             txt_date = ujson.load(f, encoding='utf-8')
#             return [item for item in txt_date if item['_Vacancy__experience'] == experience]
#
#     def jobs_deleting(self, jobs: dict) -> None:
#         """
#         Метод на удаление выбранной вакансии
#         :param jobs: словарь вакансии
#         :return: None
#         """
#         try:
#             with open(self.file, 'rb') as f:
#                 txt_date = ujson.load(f, encoding='utf-8')
#                 txt_date.remove(jobs)
#             with open(self.file, 'wb') as f:
#                 ujson.dump(txt_date, f)
#         except ValueError:
#             print('Все вакансии удалены')
#
#     def file_cleaning(self) -> None:
#         """
#         Очищение файла от вакансий
#         :return: None
#         """
#         os.remove(self.file)
# json_saver = Json_Saver()
#
# job1 = {
#     'name': 'Software Engineer',
#     'salary': 5000,
#     'experience': '3 years',
#     'city': 'New York',
#     'url': 'example.com',
#     'requirement': 'Requirements'
# }
# json_saver.jobs_adding(job1)
#
# salary_5000 = json_saver.get_salary(5000)
# print(salary_5000)

