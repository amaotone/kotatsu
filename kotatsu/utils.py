import json
import os

from oauth2client.service_account import ServiceAccountCredentials


def get_credentials():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive',
             'https://www.googleapis.com/auth/drive.photos.readonly']
    secret = os.environ.get('GOOGLE_CLIENT', None)
    if secret is not None:
        return ServiceAccountCredentials.from_json_keyfile_dict(json.loads(
            secret), scope)
    
    return ServiceAccountCredentials.from_json_keyfile_name(
        'google_client.json', scope)
