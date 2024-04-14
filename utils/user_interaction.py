import psycopg2
from src.hh_vacancy_parcers import HHVacancionParsing
from config import config
from src.db_module import DBModule


def user_interaction(value, db_name) -> None:
    """
    Взаимодействия с пользователем, получает данные от пользователя, записывает в базу даннных
    и сортирует.
    :return: None
    """
    HHVacancionParsing(value)
    module = DBModule(db_name)
    module.create_tables()
    module.full_tables(value)


def delete_database(database_name: str) -> None:
    """
    Удаление бызы данных
    :return: None
    """
    conn = psycopg2.connect(dbname='postgres', **config())
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')

    cur.close()
    conn.close()


def create_database(database_name: str) -> None:
    """
    Создание базы данных и таблиц для сохранения данных о каналах и видео
    :return: None
    """
    conn = psycopg2.connect(dbname='postgres', **config())
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()