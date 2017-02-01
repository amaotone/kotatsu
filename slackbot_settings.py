import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_TOKEN = os.environ.get('SLACK_API_TOKEN')
default_reply = '...zzz'

PLUGINS = [
    'kotatsu'
]
