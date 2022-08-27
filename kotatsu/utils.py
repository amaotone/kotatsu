# import json
# import os

# from oauth2client.service_account import ServiceAccountCredentials as SAC


# def get_credentials():
#     scope = ['https://spreadsheets.google.com/feeds',
#              'https://www.googleapis.com/auth/drive',
#              'https://www.googleapis.com/auth/drive.photos.readonly']
#     secret = os.environ['GOOGLE_CLIENT_SECRET']
#     return SAC.from_json_keyfile_dict(json.loads(secret, strict=False), scope)
