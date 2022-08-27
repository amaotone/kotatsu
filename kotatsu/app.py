import os
import re

from fastapi import FastAPI
from slack_bolt.adapter.socket_mode.async_handler import AsyncSocketModeHandler
from slack_bolt.async_app import AsyncApp

from kotatsu.cron import anniversary
from kotatsu.response import miso_soup, tired

app = FastAPI()
bolt = AsyncApp(token=os.environ["SLACK_BOT_TOKEN"])
socket_handler = AsyncSocketModeHandler(bolt, os.environ["SLACK_APP_TOKEN"])

# register responses
bolt.message(re.compile("(つかれた|疲れた|ちかりた)"))(tired)
bolt.message(re.compile("(いちたすいち|1\+1)"))(miso_soup)
app.include_router(anniversary.router)

# event logging
@bolt.event("message")
async def handle_message_events(body, logger):
    logger.info(body)


@app.on_event("startup")
async def startup():
    await socket_handler.connect_async()
