class Vacancy:
    """
    Класс, представляющий вакансию.
    """
    def __init__(self, name: str, salary: int, experience: str,
                 address: str, employment: str, city: str,
                 url: str, requirement: str) -> None:
        """
        Инициализация нового объекта Vacancy.

        Аргументы:
                name (str): Название вакансии.
                salary (int): Зарплата для вакансии. Если None, то устанавливается значение 0.
                experience (str): Требуемый опыт работы для вакансии.
                address (str): Адрес вакансии.
                employment (str): Тип занятости для вакансии.
                city (str): Город вакансии.
                url (str): URL вакансии.
                requirement (str): Требования для вакансии.
        """
        self.name = name
        if salary is None:
            self.salary = salary
        else:
            self.salary = 0
        self.experience = experience
        self.address = address
        self.employment = employment
        self.city = city
        self.url = url
        self.requirement = requirement

    @property
    def salary(self):
        """
        Зарплата для вакансии.
        Возвращает:
            int: Зарплата для вакансии.
        """
        return self.salary

    def __gt__(self, other):
        """
                Перегрузка оператора > для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет большую зарплату, иначе False.
                """
        return self.salary > other.salary

    def __ge__(self, other):
        """
                Перегрузка оператора >= для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет большую или равную зарплату, иначе False.
                """
        return self.salary >= other.salary

    def __lt__(self, other):
        """
                Перегрузка оператора < для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет меньшую зарплату, иначе False.
                """
        return self.salary < other.salary

    def __le__(self, other):
        """
                Перегрузка оператора <= для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет меньшую или равную зарплату, иначе False.
                """
        return self.salary <= other.salary

    def __eq__(self, other):
        """
                Перегрузка оператора == для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет равную зарплату, иначе False.
                """
        return self.salary == other.salary

    def __str__(self):
        """
                Представление вакансии в виде строки.

                Возвращает:
                    str: Строковое представление вакансии.
                """
        return f'{self.name}, {self.salary}, {self.experience}, ' \
               f'{self.address}, {self.employment},' \
               f'{self.city}, {self.url}, {self.requirement}'

    def __repr__(self):
        """
               Представление вакансии в виде строки.

               Возвращает:
                   str: Строковое представление вакансии.
               """
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.salary}, '{self.experience}'," \
               f"'{self.address}', '{self.employment}', " \
               f"'{self.city}', '{self.url}', '{self.requirement}')"

    @salary.setter
    def salary(self, value):
        self._salary = value

#
# vacancy = Vacancy("Software Engineer", 5000, "3 years", "123 Main St", "Full-time", "City", "example.com", "Requirements")
# print(vacancy)