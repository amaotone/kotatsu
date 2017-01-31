import json
import os

import gspread
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials
from slackbot.bot import listen_to

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


@listen_to(r'^(?:ごはん|ご飯)$')
def show(message):
    sheet = get_sheet()
    places = np.array(sheet.get_all_values())
    names = places[:, 0]
    weights = places[:, 1].astype(np.float)
    p = weights / weights.sum()
    message.send('{}はどうですか？'.format(np.random.choice(names, p=p)))
    return


@listen_to(r'^(?:ごはん|ご飯)追加[\s　]*(.*)$')
def add(message, place):
    sheet = get_sheet()
    if place in sheet.col_values(1):
        message.send('{}は既にリストに入っています'.format(place))
        return
    
    sheet.insert_row([place, 3])
    message.send('{}を追加しました(優先度3)'.format(place))
    return
