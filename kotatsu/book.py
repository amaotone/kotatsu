import json
import os

from bottlenose import api
from bs4 import BeautifulSoup
from slackbot.bot import listen_to


def fetch_book_data(word):
    key = os.environ['AMAZON_KEY']
    secret = os.environ['AMAZON_SECRET']
    tag = os.environ['AMAZON_ASSOCIATE_TAG']
    
    # TODO: 例外処理してないからよわい
    amazon = api.Amazon(key, secret, tag, Region='JP')
    res = amazon.ItemSearch(Keywords=word, SearchIndex='Books',
                            ResponseGroup='Medium')
    res = BeautifulSoup(res, 'lxml')
    
    return [{
        'title': res.title.text,
        'text': res.author.text,
        'image_url': res.largeimage.url.text,
        'fields': [
            {
                'title': res.lowestnewprice.formattedprice.text,
                'value': 'https://www.amazon.co.jp/dp/{}'.format(res.asin.text),
                'short': False
            }
        ]
    }]


@listen_to('^(?:本|ほん|book)[\s　]+(.*)')
def book(message, word):
    message.send_webapi('', json.dumps(fetch_book_data(word)))
