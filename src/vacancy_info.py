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
        self.__name = name
        if salary is None:
            self.__salary = salary
        else:
            self.__salary = 0
            self.__experience = experience
            self.__address = address
            self.__employment = employment
            self.__city = city
            self.__url = url
            self.__requirement = requirement

    @property
    def salary(self):
        """
        Зарплата для вакансии.
        Возвращает:
            int: Зарплата для вакансии.
        """
        return self.__salary

    def __gt__(self, other):
        """
                Перегрузка оператора > для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет большую зарплату, иначе False.
                """
        return self.__salary > other.__salary

    def __ge__(self, other):
        """
                Перегрузка оператора >= для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет большую или равную зарплату, иначе False.
                """
        return self.__salary >= other.__salary

    def __lt__(self, other):
        """
                Перегрузка оператора < для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет меньшую зарплату, иначе False.
                """
        return self.__salary < other.__salary

    def __le__(self, other):
        """
                Перегрузка оператора <= для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет меньшую или равную зарплату, иначе False.
                """
        return self.__salary <= other.__salary

    def __eq__(self, other):
        """
                Перегрузка оператора == для сравнения вакансий по зарплате.

                Аргументы:
                    other (Vacancy): Другой объект Vacancy для сравнения.

                Возвращает:
                    bool: True, если текущая вакансия имеет равную зарплату, иначе False.
                """
        return self.__salary == other.__salary

    def __str__(self):
        """
                Представление вакансии в виде строки.

                Возвращает:
                    str: Строковое представление вакансии.
                """
        return f'{self.__name}, {self.__salary}, {self.__experience}, ' \
               f'{self.__address}, {self.__employment},' \
               f'{self.__city}, {self.__url}, {self.__requirement}'

    def __repr__(self):
        """
               Представление вакансии в виде строки.

               Возвращает:
                   str: Строковое представление вакансии.
               """
        return f"{self.__class__.__name__}('{self.__name}', " \
               f"{self.__salary}, '{self.__experience}'," \
               f"'{self.__address}', '{self.__employment}', " \
               f"'{self.__city}', '{self.__url}', '{self.__requirement}')"


#
# vacancy = Vacancy("Software Engineer", 5000, "3 years", "123 Main St", "Full-time", "City", "example.com", "Requirements")
# print(vacancy)