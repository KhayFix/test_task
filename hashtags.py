# encode:utf-8
from datetime import datetime
import logging
import os
import re
import sys
from collections import Counter

logging.basicConfig(
    filename=f"{os.getcwd()}/logs/{datetime.now().strftime('%Y-%m-%d_%H_%M_%S')}.log",
    level=logging.INFO,
    filemode='w',
    format='%(levelname)s %(asctime)s : %(message)s',
)


def reading_data_of_test_file(file_name: str) -> list or bool:
    """
    Функция открывает тестовый файл и полностью загружает его в память.
    При успешном открытии и чтении:
    :return: list
    В случае если файл не найден:
    :return: False
    """
    try:
        with open(f"{os.getcwd()}/input_data/{file_name}", "r", encoding='utf-8') as test_file:
            text = test_file.readlines()
    except FileNotFoundError as error:
        logging.error(error)
        return False
    else:
        logging.info(text)
        return text


def top_hashtag():
    pass


if __name__ == "__main__":
    print(reading_data_of_test_file('in.txt'))
