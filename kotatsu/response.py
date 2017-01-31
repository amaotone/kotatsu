from slackbot.bot import listen_to

@listen_to('疲れた')
@listen_to('つかれた')
def rps(message):
    message.send('おつかれ:blush:')

    
@listen_to('1\+1')
@listen_to('いちたすいち')
def msp(message):
    message.send(':miso:みそスープ')
