import datetime
from slacker import Slacker
import slackbot_settings


def anv():
    today = datetime.date.today()
    (yr, mt, dy) = (today.year, today.month, today.day)

    if dy == 18:
        if yr == 2017 and mt == (3 or 6):
            return "今日は付き合い始めてから{}ヶ月です!".format(mt)
        elif mt == 12:
            return "今日は付き合い始めてから{}年です!".format(yr - 2016)


slack = Slacker(slackbot_settings.API_TOKEN)
message = anv()
slack.chat.post_message('try', message, as_user=True)
