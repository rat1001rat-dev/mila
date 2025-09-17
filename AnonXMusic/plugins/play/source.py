import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["السورس","ياسورس","يا سورس","سورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://i.postimg.cc/3J9nB1yZ/image.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻](https://t.me/YamenThon)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @T_A_Tl ❫
◉ 𝙸𝙳      : ❪ 5571722913 ❫
◉ 𝙱𝙸𝙾    : ❪ ​ﮮ اخبروا من #يظن_نفسه "#قصة_كبيرة ، باننا لا نقرأ #الروايات.🦦🖇بـ ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ ", url=f"https://t.me/T_A_Tl"), 
                 ],[
                   InlineKeyboardButton(
                        "☭ 𝗬𝗮𝗺𝗲𝗻𝗧𝗵𝗼𝗻 ☭", url=f"https://t.me/YamenThon"),
                ],

            ]

        ),

    )
