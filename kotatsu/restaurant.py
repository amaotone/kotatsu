from slackbot.bot import listen_to


@listen_to('ごはん')
@listen_to('ご飯')
def restaurant(message):
    message.send('ご飯の候補: ')
