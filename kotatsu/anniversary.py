import os
import datetime
from slacker import Slacker
import slackbot_settings

ANV_Y = os.environ.get('ANV_Y', None)
ANV_M = os.environ.get('ANV_M', None)
ANV_D = os.environ.get('ANV_D', None)


def dif(a, b):
    y = a[0] - b[0]
    m = a[1] - b[1]
    if m < 0:
        (y, m) = (y - 1, m + 12)
    return (y, m)


def anv():
    today = datetime.date.today()
    (yr, mt) = dif([today.year, today.month], [ANV_Y, ANV_M])
    dy = today.day - ANV_D

    if dy == 0:
        if yr == 0 and mt == (3 or 6):
            return "今日は付き合い始めてから{}ヶ月です!".format(mt)
        elif mt == 0:
            return "今日は付き合い始めてから{}年です!".format(yr)


slack = Slacker(slackbot_settings.API_TOKEN)
message = anv()
slack.chat.post_message('try', message, as_user=True)
