import requests, re
from AnonXMusic import app
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus, MessageMediaType



API_URL = "https://atared.serv00.net/api/chatgpt3.5.php?text="

def clean_response(text, lang='ar'):
    replace_words = ['chat gpt', 'chatgpt', 'gpt', 'open ai', 'openai', 'ai']
    for word in replace_words:
        text = re.sub(rf'(?i)\b{re.escape(word)}\b', 'ذكاء' if lang == 'ar' else 'yemen', text)
    
    text = text.replace('\\n', '\n').replace('**', '').replace('""', '"').replace('``', '').replace('###', '').replace('__', '')
    return text

def is_admin_or_owner(client, user_id, chat_id):
    try:
        member = client.get_chat_member(chat_id, user_id)
        return member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
    except:
        return False

@app.on_message(filters.regex("^ذكاء (.*)") & filters.group)
def hams(client, m: Message):
    text = m.text.split(" ", 1)[1]
    response = requests.get(f"{API_URL}{text}")
    
    if response.status_code != 200:
        return m.reply("⌯ فشل في الاتصال بالخادم.")
    
    try:
        data = response.json()
        if not data.get("status"):
            return m.reply("⌯ حدث خطأ في الاستجابة.")
        
        reply_text = clean_response(data["response"], lang='ar')
        m.reply(reply_text)
    except Exception as e:
        m.reply(f"{str(e)}")