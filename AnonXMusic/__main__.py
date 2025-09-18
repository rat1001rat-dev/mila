import asyncio
import importlib
import glob

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AnonXMusic import LOGGER, app, userbot
from AnonXMusic.core.call import Anony
from AnonXMusic.misc import sudo
from AnonXMusic.plugins import ALL_MODULES
from AnonXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

import redis
import requests

r = redis.Redis('localhost', decode_responses=True)

from information import token, owner_id

hmshelp = token.split(':')[0]
r.set(f'{hmshelp}botowner', owner_id)

username = requests.get(f"https://api.telegram.org/bot{token}/getMe").json()["result"]["username"]
r.set(f'{hmshelp}botusername', username)

if not r.get(f'{hmshelp}:botkey'):
    r.set(f'{hmshelp}:botkey', '⇜')
if not r.get(f'{hmshelp}botname'):
    r.set(f'{hmshelp}botname', 'الين')
if not r.get(f'{hmshelp}botchannel'):
    r.set(f'{hmshelp}botchannel', 'ELLNEVIP_BOT')


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    # تشغيل البوت الأساسي
    await app.start()

    # استيراد جميع موديولات الميوزك
    for all_module in ALL_MODULES:
        importlib.import_module("AnonXMusic.plugins" + all_module)
    LOGGER("AnonXMusic.plugins").info("✅ Music Modules Loaded Successfully")

    # استيراد موديولات الحماية
    for file in glob.glob("AnonXMusic/security_plugins/*.py"):
        importlib.import_module(file[:-3].replace("/", "."))
    LOGGER("AnonXMusic.security_plugins").info("✅ Security Modules Loaded Successfully")

    # تشغيل يوزربوت ومكالمات الجروبات
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("AnonXMusic").error(
            "❌ شغل مكالمة فيديو في الجروب/القناة اللوج.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()

    LOGGER("AnonXMusic").info(
        "🎵 AnonX Music Bot + 🛡️ Security Plugins Started Successfully"
    )

    # البقاء على التشغيل
    await idle()

    # إيقاف عند الخروج
    await app.stop()
    await userbot.stop()
    LOGGER("AnonXMusic").info("Bot Stopped...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
