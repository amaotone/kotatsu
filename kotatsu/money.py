import os
import psycopg2
import urllib.parse as urlparse
from slackbot.bot import listen_to


def database():
    data_url = urlparse.urlparse(os.environ['DATABASE_URL'])
    conn = psycopg2.connect(
        dbname = data_url.path[1:],
        user = data_url.username,
        password = data_url.password,
        host = data_url.hostname,
        port = data_url.port
    )
    return conn

def change_val(amount):
    conn = database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM money")
    cursor.execute("UPDATE money SET num = " + str(amount))

    conn.commit()
    cursor.close()
    conn.close()

    return

def fetch_val():
    conn = database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM money")
    num = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return num

@listen_to(r'^(?:(-?\d*)?)$')
def add(message, amount):
    now = fetch_val()
    new = now + int(amount)
    change_val(new)

    message.send('追加しました: {} -> {}'.format(now, new))

    return

@listen_to(r'^(?:reset|リセット)$')
def reset(message):
    now = fetch_val()
    change_val(0)

    message.send('リセットしました: {} -> 0'.format(now))

    return

@listen_to(r'^(?:いくら)$')
def out(message):
    now = fetch_val()

    if 250<=int(now*0.4)%500:
        now = int(now*0.4)-int(now*0.4)%500+500
    else:
        now = int(now*0.4)-int(now*0.4)%500

    message.send('支払い金額: {}'.format(now))

    return

