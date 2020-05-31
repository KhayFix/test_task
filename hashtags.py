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

    В случае если файл не найден:
    :return: False.
    При успешном открытии и чтении:
    :return: list.
    """
    try:
        with open(f"{os.getcwd()}/input_data/{file_name}", "r", encoding='utf-8') as test_file:
            text = test_file.readlines()
    except FileNotFoundError as error:
        logging.error(error)
        return False
    else:
        logging.info(f"Received data: {text}")
        return text


def top_hash_tag(tweet: list, hash_tag_count: int = 10) -> list or bool:
    """
    Функция определяет массив хэштегов, наиболее часто встречающихся во входных данных.
    Массив отсортирован по частоте в убывающем порядке.

    :param tweet: Входные данные для анализа.
    :param hash_tag_count: Колличество самых популярных хэштегов, которое возвращается пользователю.
    :return: В случае возникновения ошибки вернет: False.
    :return: Возвращается ['iphone', 'apple', 'igers'...] при успешной обработке данных.
    """
    try:
        hash_tag = [re.findall(r"#(\w+)", str(text).lower()) for text in tweet]
        frequent_hash_tag = Counter([text for sublist in hash_tag for text in sublist]).most_common(hash_tag_count)
        result = [key for key, value in frequent_hash_tag]  # получаем отсортированные по убыванию популярные хэштеги
    except (TypeError, AttributeError) as error:
        logging.error(error)
        return False
    else:
        logging.info(f"Sorted by data descending: {result}")
        return result


def commonly_used_tweets_words(tweet: list, top_hash_tags: list, word_count: int = 5) -> dict or bool:
    """
    Функция определяет списки самых значимых слов в твитах,
    слов только для топ наиболее популярных хэштегов.

    :param tweet: Входные данные для анализа.
    :param top_hash_tags: Наиболее часто встречающиеся хэштеги во входных данных.
    :param word_count: Колличество значимых слов, наиболее часто встречающихся в твитах.
    :return: В случае возникновения ошибки вернет: False.
    :return: Возвращается {'iphone': ['for', 'and', 'like', 'android', 'retweet' ...], ...}
     при успешной обработке.
    """
    often_used_words = {}
    try:
        for hash_tag in top_hash_tags:
            sorted_tweets_by_hash_tags = [re.sub(r'#[A-Za-z]+', '', str(text).lower())
                                          for text in tweet if hash_tag in str(text).lower()
                                          ]

            breakdown_into_words = [re.findall(r'\b[a-zA-Z]{2,15}\b', tweets)
                                    for tweets in sorted_tweets_by_hash_tags
                                    ]
            top_words = Counter(
                [word for tweet_words in breakdown_into_words
                 for word in tweet_words]).most_common(word_count)

            sorted_words = [word for word, value in top_words]
            often_used_words[hash_tag] = sorted_words

    except (TypeError, AttributeError) as error:
        logging.error(error)
        return False
    else:
        logging.info(f"Word lists for top popular hashtags: {often_used_words}")
        return often_used_words


def run(name_file: str = 'in.txt'):
    """Функция возвращает полученные данные в stdout"""

    tweets = reading_data_of_test_file(name_file)
    hash_tag = top_hash_tag(tweet=tweets)
    words = commonly_used_tweets_words(tweet=tweets, top_hash_tags=hash_tag)

    return sys.stdout.write(f"{str(hash_tag)}\n{str(words)}")


if __name__ == "__main__":
    run()
