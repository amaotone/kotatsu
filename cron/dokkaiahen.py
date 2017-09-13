import os
import sys
import json

from pyquery import PyQuery as pq
from slacker import Slacker

sys.path.append(os.path.abspath(os.curdir))

from slackbot_settings import API_TOKEN


def dokkaiahen():
    base_url = 'http://dka-hero.com/'
    page = pq(url=base_url + 't_c.html', encoding='shift_jis')
    link = page('a:first')
    
    with open('horimiya.json','r') as f:
        horimiya = json.load(f)
        old = horimiya['title']
    new = link.text()
    
    if new != old:
        with open('horimiya.json','w') as f:
            horimiya['title'] = new
            json.dump(horimiya,f)
        return {'title': new, 'link': base_url + link.attr('href')}
    
    else:
        print('There is no update on {}'.format(base_url))


if __name__ == '__main__':
    slack = Slacker(API_TOKEN)
    res = dokkaiahen()
    if res:
        message = '読解アヘンに更新があります\n{title}\n{link}'.format(**res)
        slack.chat.post_message('#try', message, as_user=True)
