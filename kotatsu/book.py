import json
import os
import random
import time
from urllib.error import HTTPError

from bottlenose import api
from bs4 import BeautifulSoup
from slackbot.bot import listen_to


def error_handler(err):
    ex = err['exception']
    if isinstance(ex, HTTPError) and ex.code == 503:
        time.sleep(random.expovariate(0.1))
        return True


def fetch_book_data(word):
    key = os.environ['AMAZON_KEY']
    secret = os.environ['AMAZON_SECRET']
    tag = os.environ['AMAZON_ASSOCIATE_TAG']
    
    amazon = api.Amazon(key, secret, tag, Region='JP',
                        ErrorHandler=error_handler)
    res = amazon.ItemSearch(Keywords=word, SearchIndex='Books',
                            ResponseGroup='Medium')
    res = BeautifulSoup(res, 'lxml')
    
    if res.totalresults.text == '0':
        raise RuntimeError('Search resullts could not be found.')
    
    return [{
        'title': res.title.text,
        'title_link': res.detailpageurl.text,
        'text': res.author.text,
        'image_url': res.largeimage.url.text
    }]


@listen_to('^(?:本|ほん|book)[\s　]+(.*)')
def book(message, word):
    try:
        message.send_webapi('', json.dumps(fetch_book_data(word)))
    except RuntimeError:
        message.send('検索結果が見つかりませんでした :sweat_drops:')
