from slackbot.bot import listen_to

@listen_to('疲れた')
@listen_to('つかれた')
def rps(message):
    message.send('おつかれ:blush:')
