import json
import os

import httplib2
import numpy as np
from apiclient import discovery
from slackbot.bot import listen_to

from .utils import get_credentials


@listen_to('^(?:しゃしん|写真)$')
def photo(message):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    send_user = message.channel._client.users[message.body['user']]['name']
    
    user_album = json.loads(os.environ['USER_ALBUM'])
    
    response = service.files().list(spaces='drive', pageSize=1000).execute()
    files = response.get('files', [])
    photos = [f['id'] for f in files if
              ('.jpg' in f['name']) and (f['id'][2] != user_album[send_user])]
    photo_id = np.random.choice(photos)
    
    url = 'http://drive.google.com/uc?export=view&id={}'.format(photo_id)
    
    message.send(url)
