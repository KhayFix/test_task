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


def top_hash_tag(quantity: int = 10):
    texts = reading_data_of_test_file('in.txt')

    hash_tag = [re.findall(r"#(\w+)", text.lower()) for text in texts]
    hash_tag = Counter([text for sublist in hash_tag for text in sublist])
    frequent_hash_tag = hash_tag.most_common(quantity)

    result = [key for key, value in frequent_hash_tag]  # получаем отсортированные по убыванию популярные хэштеги
    logging.info(f"Sorted by data descending: {result}")

    often_used_words = {}
    for top_hash_tags in result:
        sorted_tweets_by_hash_tags = [re.sub(r'#[A-Za-z]+', '', text.lower())
                                      for text in texts if top_hash_tags in text.lower()
                                      ]

        breakdown_into_words = [re.findall(r'\b[a-zA-Z]{2,15}\b', tweets)
                                for tweets in sorted_tweets_by_hash_tags
                                ]
        top_words = Counter(
            [word for tweet_words in breakdown_into_words
             for word in tweet_words]).most_common(5)

        sorted_words = [word for word, value in top_words]
        often_used_words[top_hash_tags] = sorted_words

    return sys.stdout.write(f"{str(result)}\n{str(often_used_words)}")


if __name__ == "__main__":
    top_hash_tag()
