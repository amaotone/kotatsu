import os
import sys
import psycopg2
import urllib.parse as urlparse

from pyquery import PyQuery as pq
from slacker import Slacker

sys.path.append(os.path.abspath(os.curdir))

from slackbot_settings import API_TOKEN


def dokkaiahen():
    base_url = 'http://dka-hero.com/'
    page = pq(url=base_url + 't_c.html', encoding='shift_jis')
    link = page('a:first')

    data_url = urlparse.urlparse(os.environ['DATABASE_URL'])
    conn = psycopg2.connect(
        dbname = data_url.path[1:],
        user = data_url.username,
        password = data_url.password,
        host = data_url.hostname,
        port = data_url.port
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM horimiya")
    old = cursor.fetchone()[0]
    
    newtext = link.text()
    new = ascii(newtext).strip("'")

    if repr(new).strip("'") != old:
        cursor.execute("UPDATE horimiya SET title = " + repr(new))
        li = {'title': newtext, 'link': base_url + link.attr('href')}
            
    else:
        print('There is no update on {}'.format(base_url))
        li = {}

    conn.commit()
    cursor.close()
    conn.close()

    return li

if __name__ == '__main__':
    slack = Slacker(API_TOKEN)
    res = dokkaiahen()
    if res:
        message = '読解アヘンに更新があります\n{title}\n{link}'.format(**res)
        slack.chat.post_message('#try', message, as_user=True)
