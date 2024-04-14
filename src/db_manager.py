import psycopg2
from config import config


class DBManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = psycopg2.connect(dbname=self.db_name, **config())

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT employer_name, COUNT(vacancy_name) FROM vacancies JOIN employer '
                               'ON employer.employer_id=vacancies.company_id GROUP BY employer_name '
                               'ORDER BY COUNT(vacancy_name) DESC')
                data = cursor.fetchall()
                print(data)

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT employer_name, vacancy_name, salary_from, salary_to, url FROM vacancies  '
                               'JOIN employer ON employer.employer_id=vacancies.company_id ORDER BY employer_name')
                data = cursor.fetchall()
                print(data)

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT vacancy_name, AVG(salary_from) FROM vacancies GROUP BY vacancy_name')
                data = cursor.fetchall()
                print(data)

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute('SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies) '
                               'ORDER BY salary_from')
                data = cursor.fetchall()
                print(data)

    def get_vacancies_with_keyword(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        """
        with self.conn:
            with self.conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM vacancies WHERE vacancy_name LIKE '%{keyword}%'")
                data = cursor.fetchall()
                print(data)