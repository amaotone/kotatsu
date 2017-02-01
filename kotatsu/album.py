import json
import os

import httplib2
import numpy as np
from apiclient import discovery
from slackbot.bot import listen_to

from .utils import get_credentials

alb = os.environ.get('ALB', None)

if alb is not None:
    alb = json.loads(alb)
else:
    with open("user_config.json") as file:
        alb = json.load(file)


@listen_to('^(?:しゃしん|写真)$')
def photo(message):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    send_user = message.channel._client.users[message.body['user']]['name']

    results = service.files().list(spaces='drive', pageSize=1000).execute().get(
        'files', [])
    photos = [res['id'] for res in results if ('.jpg' in res['name']) and (res['id'][2] != alb[send_user])]
    photo_id = np.random.choice(photos)

    url = 'http://drive.google.com/uc?export=view&id={}'.format(photo_id)

    message.send(url)
