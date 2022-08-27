# import json
# import os
# import unicodedata

# import httplib2
# import numpy as np
# from apiclient import discovery
# from slackbot.bot import listen_to

# from .utils import get_credentials


# @listen_to(r'^(?:しゃしん|写真|photo)(?:$|[\s　]+(\d*)?)')
# def photo(message, number):
#     if not number:
#         number = 1
#     else:
#         number = int(unicodedata.normalize('NFKC', number))

#     credentials = get_credentials()
#     http = credentials.authorize(httplib2.Http())
#     service = discovery.build('drive', 'v3', http=http)
#     user_name = message.channel._client.users[message.body['user']]['name']
#     user_album = json.loads(os.environ['USER_ALBUM'])[user_name]

#     files = []
#     page_token = None
#     while True:
#         response = service.files().list(
#             spaces='drive',
#             q="mimeType='image/jpeg' and not ('{}' in parents)".format(
#                 user_album),
#             fields='nextPageToken, files(id)',
#             pageToken=page_token,
#             pageSize=1000).execute()
#         files += response.get('files', [])
#         page_token = response.get('nextPageToken', None)
#         if page_token is None:
#             break

#     if files:
#         url = 'http://drive.google.com/uc?export=view&id={}'
#         attachments = [{'text': '', 'image_url': url.format(f['id'])} for f in
#                        np.random.choice(files, size=number)]
#         message.send_webapi('', json.dumps(attachments))
#     else:
#         message.send('写真が見つかりませんでした :sweat_drops:')
