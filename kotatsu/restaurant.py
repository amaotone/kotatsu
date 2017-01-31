import json
import os

import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from slackbot.bot import listen_to, respond_to

GOOGLE_CLIENT = os.environ.get('GOOGLE_CLIENT', None)
RESTAURANT_SHEET = os.environ.get('RESTAURANT_SHEET', None)


def get_credentials():
    scope = ['https://spreadsheets.google.com/feeds']
    if GOOGLE_CLIENT is not None:
        return ServiceAccountCredentials.from_json_keyfile_dict(json.loads(
            GOOGLE_CLIENT), scope)
    
    return ServiceAccountCredentials.from_json_keyfile_name(
        'google_client.json', scope)


def get_sheet():
    credentials = get_credentials()
    client = gspread.authorize(credentials)
    file = client.open_by_key(RESTAURANT_SHEET)
    sheet = file.sheet1
    return sheet


def choose():
    sheet = get_sheet()
    records = np.array(sheet.get_all_values())
    names = records[:, 0]
    weights = records[:, 1].astype(np.float)
    p = weights / weights.sum()
    return np.random.choice(names, p=p)


@respond_to('ごはん')
@respond_to('ご飯')
@listen_to('ごはん')
@listen_to('ご飯')
def restaurant(message):
    message.send('{}はどうですか？'.format(choose()))
