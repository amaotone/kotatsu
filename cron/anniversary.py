import datetime
import os
import sys

from slacker import Slacker

sys.path.append(os.path.abspath(os.curdir))

from slackbot_settings import API_TOKEN


def diff(a, b):
    y = a[0] - b[0]
    m = a[1] - b[1]
    if m < 0:
        (y, m) = (y - 1, m + 12)
    return (y, m)


def anniversary():
    ANV_Y = int(os.environ.get('ANV_Y', None))
    ANV_M = int(os.environ.get('ANV_M', None))
    ANV_D = int(os.environ.get('ANV_D', None))
    
    today = datetime.date.today()
    (yr, mt) = diff([today.year, today.month], [ANV_Y, ANV_M])
    dy = today.day - ANV_D
    
    if dy == 0:
        if yr == 0 and mt == (3 or 6):
            return "今日は付き合い始めてから{}ヶ月です!".format(mt)
        elif mt == 0:
            return "今日は付き合い始めてから{}年です!".format(yr)
    
    return ""


if __name__ == '__main__':
    slack = Slacker(API_TOKEN)
    message = anniversary()
    if message:
        slack.chat.post_message('#general', message, as_user=True)
