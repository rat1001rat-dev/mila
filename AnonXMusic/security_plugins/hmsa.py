from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AnonXMusic import app
import uuid
import redis

wsdb = redis.Redis(decode_responses=True)  # استخدم نفس قاعدة البيانات

@app.on_message(filters.text & filters.reply & filters.group)
async def whisper(_, m):
    text = m.text.strip()
    if text == "همسه" and m.reply_to_message and m.reply_to_message.from_user:
        user_id = m.reply_to_message.from_user.id
        if user_id == m.from_user.id:
            return await m.reply("⌯ مافيك تهمس لنفسك 🙂")
        
        whisper_id = str(uuid.uuid4())[:6]
        sent = await m.reply(
            f"⌯ تم تحديد الهمسة إلى [ {m.reply_to_message.from_user.mention} ]\n\n"
            f"~ اضغط على الزر بالأسفل لإرسال الهمسة",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ارسال الهمسة",
                            url=f"t.me/{(await app.get_me()).username}?start=hmsa{whisper_id}",
                        )
                    ]
                ]
            ),
        )
        data = {
            "from": m.from_user.id,
            "to": user_id,
            "chat": m.chat.id,
            "id": sent.id,
        }
        wsdb.setex(whisper_id, 3600, str(data))  # يخزنها لساعة
