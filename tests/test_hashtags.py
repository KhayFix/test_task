# encode: utf-8

from hashtags import commonly_used_tweets_words, reading_data_of_test_file, top_hash_tag


def test_reading_data_of_test_file():
    assert type(reading_data_of_test_file('in.txt')) == list
    assert reading_data_of_test_file('no file') is False


def test_top_hash_tag():
    tweets1 = ['#Apple #Apple iOS 14 beta', '#iphone Like for #iphone, retweet for ios.']
    tweets2 = ['#Apple Apple iOS 14 beta', '#iphone Like for #iphone, retweet for ios.']

    assert top_hash_tag(tweets1) == ['apple', 'iphone']
    assert top_hash_tag(tweets2) == ['iphone', 'apple']
    assert top_hash_tag(tweet=[1, 2, 3]) == []
    assert top_hash_tag(tweet=['Like for android, retweet for ios']) == []
    assert top_hash_tag(tweet=1) is False
    assert top_hash_tag(tweet='1') == []


def test_commonly_used_tweets_words():
    tweets = ['#Apple Apple iOS 14 beta, beta', '#iphone Like for #iphone, retweet for ios, ios.']
    hash_tag = ['iphone', 'apple']
    assert commonly_used_tweets_words(tweet=tweets, top_hash_tags=hash_tag) == {
        'iphone': ['for', 'ios', 'like', 'retweet'],
        'apple': ['beta', 'apple', 'ios'],
    }
    assert commonly_used_tweets_words(tweet=['Apple iOS 14 beta, beta'], top_hash_tags=['apple']) == {
        'apple': ['beta', 'apple', 'ios'],
    }
    assert commonly_used_tweets_words(tweet=[1, 2, 3, 4], top_hash_tags=hash_tag) == {'iphone': [], 'apple': []}
    assert commonly_used_tweets_words(
        tweet=['Like for, retweet for ios, ios.'], top_hash_tags=[1, 2, 3, 4]
    ) is False

    assert commonly_used_tweets_words(tweet=1, top_hash_tags=hash_tag) is False
    assert commonly_used_tweets_words(tweet=tweets, top_hash_tags=1) is False
