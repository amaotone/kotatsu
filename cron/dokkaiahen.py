import os
import sys

from pyquery import PyQuery as pq
from slacker import Slacker

sys.path.append(os.path.abspath(os.curdir))

from slackbot_settings import API_TOKEN


def dokkaiahen():
    base_url = 'http://dka-hero.com/'
    page = pq(url=base_url + 't_c.html', encoding='shift_jis')
    link = page('a:first')
    
    old = os.environ.get('HORIMIYA', '')
    new = link.text()
    
    if new != old:
        os.environ['HORIMIYA'] = new
        return {'title': new, 'link': base_url + link.attr('href')}
    
    else:
        print('There is no update on {}'.format(base_url))


if __name__ == '__main__':
    slack = Slacker(API_TOKEN)
    res = dokkaiahen()
    if res:
        message = '読解アヘンに更新があります\n{title}\n{link}'.format(**res)
        slack.chat.post_message('#kotatsu_test', message, as_user=True)
