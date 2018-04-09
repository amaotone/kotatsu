import os
from slackbot.bot import listen_to

@listen_to(r'^(?:(\d*)?)$')
def add(message, amount):
    now = int(os.environ.get('MONEY', '0'))
    new = now + int(amount)
    os.environ['MONEY'] = str(new)

    message.send('追加しました: {} -> {}'.format(now, new))
    return

@listen_to(r'^(?:reset|リセット)$')
def reset(message):
    now = int(os.environ.get('MONEY', '0'))
    os.environ['MONEY'] = '0'

    message.send('リセットしました: {} -> 0'.format(now))
    return

@listen_to(r'^(?:いくら)$')
def out(message):
    now = int(os.environ.get('MONEY', '0'))
    if 250<=int(now*0.4)%500:
        now = int(now*0.4)-int(now*0.4)%500+500
    else:
        now = int(now*0.4)-int(now*0.4)%500

    message.send('支払い金額: {}'.format(now))
    return

