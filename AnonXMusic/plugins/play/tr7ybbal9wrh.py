from pyrogram import Client, filters, types
from datetime import datetime
import asyncio 
from AnonXMusic import app


chat_id = -1002713260757

welcome_photo = "path_to_your_welcome_photo.jpg"


@app.on_message(filters.new_chat_members & filters.group)
async def welcome_new_members(client, message):
    for member in message.new_chat_members:
        await message.reply_photo(welcome_photo, f"اهلا وسهلا {member.first_name} منور كروبنا!")

