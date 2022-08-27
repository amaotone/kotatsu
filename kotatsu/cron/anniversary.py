import asyncio
import os
from datetime import datetime

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter

router = APIRouter()


def create_message():
    anniversary_date = os.environ.get("ANNIVERSARY_DATE")
    anniversary_date = datetime.strptime(anniversary_date, "%Y-%m-%d")
    today = datetime.now()
    delta = relativedelta(today, anniversary_date)

    if delta.days != 0 or not (delta.years > 0 or delta.months > 0):
        return ""

    y = f"{delta.years}年" if delta.years > 0 else ""
    m = f"{delta.months}ヶ月" if delta.months > 0 else ""

    return f":tada::tada::tada:\n今日は付き合い始めて{y}{m}です！\n:tada::tada::tada:"


@router.get("/cron/anniversary")
async def post_anniversary():
    from kotatsu.app import bolt

    message = create_message()
    if message:
        await bolt.client.chat_postMessage(channel="#general", text=message)
    await asyncio.sleep(0)
