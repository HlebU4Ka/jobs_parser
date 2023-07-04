from abc import ABC, abstractmethod
import ujson
import os
import csv


class Saver_file(ABC):

    @abstractmethod
    def jobs_adding(self, jobs):
        pass

    @abstractmethod
    def get_salary(self, salary):
        pass

    @abstractmethod
    def get_city(self, citi):
        pass

    @abstractmethod
    def get_experience(self, experience):
        pass

    @abstractmethod
    def jobs_deleting(self, jobs):
        pass

    @abstractmethod
    def file_cleaning(self):
        pass


class Json_Saver(Saver_file):
    file = os.path.join("saver file", 'vacancy.json')

    def jobs_adding(self, jobs: dict) -> None:
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

    def get_salary(self, salary: int) -> list:
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item].get('_Vacancy__salary') == salary]

    def get_city(self, city: str) -> list:
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in
                    range(len(ujson_data)) if ujson_data[item]['_Vacancy__city'] == city]

    def get_experience(self, experience):
        with open(self.file, 'r', encoding="utf-8") as file:
            ujson_data = ujson.load(file)
            return [ujson_data[item] for item in range(len(ujson_data)) if
                    ujson_data[item]['_Vacancy__experience'] == experience]

    def jobs_deleting(self, jobs):
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
        os.remove(self.file)

json_saver = Json_Saver()

job1 = {
    'name': 'Software Engineer',
    'salary': 5000,
    'experience': '3 years',
    'city': 'New York',
    'url': 'example.com',
    'requirement': 'Requirements'
}
json_saver.jobs_adding(job1)

salary_5000 = json_saver.get_salary(5000)
print(salary_5000)