В рамках проекта получаем данные о компаниях и вакансиях с сайта hh.ru, проектируем таблицы в БД PostgreSQL и загружаем полученные данные в созданные таблицы. Основные шаги проекта

Получаем данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотека 'requests'
Выбирается 10 или менее интересных вам компаний, от которых вы будете получать данные о вакансиях по API.
Проектируются таблицы в БД PostgreSQL для хранения полученных данных о работодателях и их вакансиях. Для работы с БД используется библиотека 'psycopg2'
Реализцется код, который заполняет созданные в БД PostgreSQL таблицы данными о работодателях и их вакансиях.
• Создан класс DBManager для работы с данными в БД, который отвечает за запросы к уже созданной базе данных

метод 'get_companies_and_vacancies_count': Получает список всех компаний и количество вакансий у каждой компании,
метод 'get_all_vacancies': Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию,
метод 'get_avg_salary': Получает среднюю зарплату по вакансиям,
метод 'get_vacancies_with_higher_salary': Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям,
метод 'get_vacancies_with_keyword': Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
• Создан класс DBModule который отвечает за создание таблиц двух таблиц (employer, vacancies) в базе данных и заполнением этих таблиц данными с hh.ru.

метод 'create_tables': Метод создает две таблицы в базе данных 'hh_vacancies', Одна таблица называется 'employer', вторая 'vacancies' в 'employer' создаются две колонки: employer_id, employer_name. В 'vacancies' создаются шесть колонок: vacancy_id, company_id, vacancy_name, salary_from, salary_to и url,
метод 'full_tables': Метод заполнения таблиц в базе данных 'hh_vacancies', компаниями и вокансиями компаний из сайта 'Head Hunter'
• Создан класс 'HHVacancionParsing', который отвечает за парсинг сайта hh.ru по кампаниям и вакансиям.

метод 'get_request_employeers': Метод возвращающий json по умолчанию 10 компаний,
метод 'get_employers_sort': Метод сортировки 10 компаний, возвращется список с id компании, название вакансии,
метод 'get_vacancies_from_company': Метод возвращающий json вакансий,
метод 'get_all_vacancyes': Метод забирает список с метода get_employers_sort, и список get_vacancies_from_company и сортирует все вакансии по определенному id компании и складывает все в список,
метод 'filter_vacancyes': Метод фильтрации вакансий по нужному нам формату, id, name, salary_from, salary_to, url, emloyeer.
