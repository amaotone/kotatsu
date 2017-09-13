from slackbot.bot import default_reply
import requests
import os
import json

@default_reply(matchstr='(.*)')
def dialogue(message, input_text):
    url = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY='+ \
            os.environ.get('DIALOGUE_API_KEY', "")
    headers = {'content-type':'application/json'}
    data = {
            'utt':input_text,
            'mode':'dialog',
            'place':'東京'
            }
    rs = requests.post(
            url,
            data=json.dumps(data),
            headers=headers
            ).json()
    if rs.get('error'):
        message.reply(rs.get('error')['message'])
    else:
        message.reply(rs.get('utt'))
