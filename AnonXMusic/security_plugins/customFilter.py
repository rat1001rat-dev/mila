import random, re, time, pytz
from datetime import datetime
from threading import Thread
from pyrogram import *
from pyrogram.enums import *
from AnonXMusic import app
from pyrogram.types import *
from config import *
from helpers.Ranks import *


@app.on_message(filters.group, group=21)
def addCustomReplyDone(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=addreply2,args=(c,m,k)).start()
    
def addreply2(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   
   TIME_ZONE = "Asia/Riyadh"
   ZONE = pytz.timezone(TIME_ZONE)
   TIME = datetime.now(ZONE)
   date = TIME.strftime("%d/%m/%Y %I:%M:%S %p")
   
   if m.text:
     if m.text == 'الغاء' and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}'):
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
       m.reply(f'{k} من عيوني لغيت اضافة الرد')
     
     if r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
       text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
       r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type=text&text={m.text.html}')
       r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','نص')
       r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
       r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
       r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
       return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.photo and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'photo'
      photo = m.photo.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&photo={photo}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','صوره')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.video and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'video'
      video = m.video.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&video={video}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','فيديو')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.animation and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'animation'
      anim = m.animation.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&animation={anim}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','متحركه')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.audio and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'audio'
      aud = m.audio.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&audio={aud}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','صوت')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.voice and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'voice'
      voice = m.voice.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&voice={voice}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','بصمه')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.document and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'doc'
      doc = m.document.file_id
      if m.caption:
        caption = m.caption.html
      else:
        caption = 'None'
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&doc={doc}&caption={caption}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','ملف')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   
   if m.sticker and r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id, m.chat.id):
      type = 'sticker'
      stic = m.sticker.file_id
      text = r.get(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      r.set(f'{text}:filter:{hmshelp}{m.chat.id}', f'type={type}&sticker={stic}')
      r.set(f'{text}:filtertype:{m.chat.id}{hmshelp}','ستيكر')
      r.set(f'{text}:filterInfo:{m.chat.id}{hmshelp}', f'by={m.from_user.id}&date={date}')
      r.sadd(f'{m.chat.id}:FiltersList:{hmshelp}', f'{text}')
      r.delete(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}')
      return m.reply(f'( {text} )\nواضفنا الرد ياحلو\n☆',parse_mode=ParseMode.HTML)
   

@app.on_message(filters.text & filters.group, group=22)
def addCustomReply(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=addreply,args=(c,m,k)).start()
    
def addreply(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return    
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'ميلا'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
   if isLockCommand(m.from_user.id, m.chat.id, text): return
   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد')
     return 
   
   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}')
     m.reply(f'{k} من عيوني لغيت مسح الرد')
     return 

   if r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
      if not r.get(f'{m.text}:filterInfo:{m.chat.id}{hmshelp}'):
        r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}')
        return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
      else:
           r.delete(f'{m.text}:filter:{hmshelp}{m.chat.id}')
           r.delete(f'{m.text}:filtertype:{m.chat.id}{hmshelp}')
           r.delete(f'{m.text}:filterInfo:{m.chat.id}{hmshelp}')
           r.srem(f'{m.chat.id}:FiltersList:{hmshelp}', m.text)
           r.delete(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}')
           return m.reply(f'( {m.text} )\n{k} وحذفنا الرد ياحلو')

   if r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
      r.set(f'{m.chat.id}:addFilter2:{m.from_user.id}{hmshelp}', m.text)
      r.delete(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}')
      m.reply(f'{k} حلو الحين ارسل جواب الرد\n{k} ( نص,صوره,فيديو,متحركه,بصمه,صوت,ملف )\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
      return 

   if text.startswith('الرد ') and len(m.text.split()) > 1 and mod_pls(m.from_user.id,m.chat.id):
      reply = m.text.split(None,1)[1]
      if not r.get(f'{reply}:filterInfo:{m.chat.id}{hmshelp}'):
        return m.reply(f'{k} الرد مو مضاف')
      else:
        get = r.get(f'{reply}:filterInfo:{m.chat.id}{hmshelp}')
        split = get.split('by=')[1]
        by = split.split('&date=')[0]
        date = split.split('&date=')[1]
        type = r.get(f'{reply}:filtertype:{m.chat.id}{hmshelp}')
        text = f'{k} الرد ↢ [{reply}](tg://user?id={by})\n{k} تاريخ الاضافة ↢\n( {date} )\n{k} نوع الرد {type}\n☆'
        m.reply(text)
        return 
   
   if text == 'تعطيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filter:{hmshelp}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filter:{hmshelp}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت الردود\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filter:{hmshelp}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} الردود مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filter:{hmshelp}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت الردود\n☆',parse_mode=ParseMode.HTML)
  
   if text == 'تعطيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if r.get(f'{m.chat.id}:lock_filterMEM:{hmshelp}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء معطله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.set(f'{m.chat.id}:lock_filterMEM:{hmshelp}',1)
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر عطلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'تفعيل ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     if not r.get(f'{m.chat.id}:lock_filterMEM:{hmshelp}'):
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ردود الاعضاء مفعله من قبل\n☆',parse_mode=ParseMode.HTML)
     else:
        r.delete(f'{m.chat.id}:lock_filterMEM:{hmshelp}')
        return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ابشر فعلت ردود الاعضاء\n☆',parse_mode=ParseMode.HTML)
   
   if text == 'ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{hmshelp}'):
       return m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
       text = 'ردود الاعضاء:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{hmshelp}'):
          rep = reply.split("&&&&")[0]
          type = reply.split("&&&&")[1]
          try:
            mention=c.get_users(int(type)).mention
          except:
            mention=f'<a href="tg://user?id={type}">{type}</a>'
          text += f'\n{count} - ( {rep} ) ࿓ ( {mention} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح ردود الاعضاء':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersListMEM:{hmshelp}'):
        return m.reply(f'{k} مافيه ردود اعضاء مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersListMEM:{hmshelp}'):
           rep = reply
           r.delete(f'{rep}:filterMEM:{hmshelp}{m.chat.id}')
           r.srem(f'{m.chat.id}:FiltersListMEM:{hmshelp}', rep)
           r.delete(f"{rep.split('&&&&')[1]}:FILT:{m.chat.id}{hmshelp}")
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من ردود الاعضاء')
   
   if text == 'الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{hmshelp}'):
       return m.reply(f'{k} مافيه ردود مضافه')
      else:
       text = 'ردود المجموعه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:FiltersList:{hmshelp}'):
          rep = reply
          type = r.get(f'{rep}:filtertype:{m.chat.id}{hmshelp}')
          text += f'\n{count} - ( {rep} ) ࿓ ( {type} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
  
   if text == 'مسح الردود':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:FiltersList:{hmshelp}'):
        return m.reply(f'{k} مافيه ردود مضافه')
      else:
        total = 0
        for reply in r.smembers(f'{m.chat.id}:FiltersList:{hmshelp}'):
           rep = reply
           r.delete(f'{rep}:filter:{hmshelp}{m.chat.id}')
           r.delete(f'{rep}:filtertype:{m.chat.id}{hmshelp}')
           r.delete(f'{rep}:filterInfo:{m.chat.id}{hmshelp}')
           r.srem(f'{m.chat.id}:FiltersList:{hmshelp}', rep)
           total += 1
        return m.reply(f'{k} ابشر مسحت ( {total} ) من الردود')
   
   if text == 'اضف ردي':
      if r.get(f'{m.chat.id}:lock_filterMEM:{hmshelp}'):
        return m.reply(f'{k} تم تعطيل ردود الأعضاء')
      if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}"):
        name = r.get(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}")
        return m.reply(f"{k} عندك رد مضاف من قبل و هو ( {name} )")
      else:
        m.reply(f'{k} حلو ، الحين ارسل اسمك')
        r.set(f'{m.chat.id}:addFilterMM:{m.from_user.id}{hmshelp}',1,ex=600)
        return 
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{hmshelp}') and text == "الغاء":
     r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{hmshelp}')
     return m.reply(f"{k} ابشر لغيت اضافة ردك")
     
   
   if r.get(f'{m.chat.id}:addFilterMM:{m.from_user.id}{hmshelp}') and len(m.text) <= 50:
     name = m.text
     if r.sismember(f'{m.chat.id}:FiltersListMEM:{hmshelp}',name):
       return m.reply(f"{k} هذا الإسم محجوز")
     else:
       r.sadd(f'{m.chat.id}:FiltersListMEM:{hmshelp}',f"{name}&&&&{m.from_user.id}")
       r.sadd(f'{m.chat.id}:FiltersListMEMM:{hmshelp}',m.from_user.id)
       r.set(f'{name}:filterMEM:{hmshelp}{m.chat.id}',m.from_user.id)
       r.set(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}",name)
       r.delete(f'{m.chat.id}:addFilterMM:{m.from_user.id}{hmshelp}')
       return m.reply(f"{k} ابشر ضفت ردك ( {name} )")
   
   if text == 'مسح ردي':
     if r.get(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}"):
       rep=r.get(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}")
       r.delete(f'{rep}:filterMEM:{hmshelp}{m.chat.id}')
       r.srem(f'{m.chat.id}:FiltersListMEM:{hmshelp}', f"{rep}&&&&{m.from_user.id}")
       r.delete(f"{m.from_user.id}:FILT:{m.chat.id}{hmshelp}")
       return m.reply(f"{k} ابشر مسحت ردك ( {rep} )")
     else:
       return m.reply(f"{k} ماعندك رد")
        
   if text == 'اضف رد':
     if not r.get(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        m.reply(f'{k} حلو ، الحين ارسل الكلمة اللي تبيها')
        r.set(f'{m.chat.id}:addFilter:{m.from_user.id}{hmshelp}',1)
        return 
        
   if text == 'مسح رد':
     if not r.get(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}'):
      if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
      else:
        r.set(f'{m.chat.id}:delFilter:{m.from_user.id}{hmshelp}',1)
        m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
        return 
   
   
   
   
   

   

@app.on_message(filters.group & filters.text, group=23)
def addCustomReplyRandom(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=addreplyrandom,args=(c,m,k)).start()
   

def addreplyrandom(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):  return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'ميلا'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
   
   if isLockCommand(m.from_user.id, m.chat.id, text): return

   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}')
     m.reply(f'{k} من عيوني لغيت اضافة الرد المميز')
     return 
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}') and text == 'الغاء':
     rep = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}')
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}')
     r.delete(f'{rep}:randomfilter:{m.chat.id}{hmshelp}')
     m.reply(f'{k} من عيوني لغيت اضافه الرد المميز')
     return 
     
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}') and text == 'الغاء':
     r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}')
     return m.reply(f'{k} من عيوني لغيت مسح الرد المميز')
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}') and text == 'تم':
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}')
     count = len(r.smembers((f'{text}:randomfilter:{m.chat.id}{hmshelp}')))
     r.set(f'{text}:randomFilter:{m.chat.id}{hmshelp}', 1)
     r.sadd(f'{m.chat.id}:RFiltersList:{hmshelp}', text)
     r.delete(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}')
     return m.reply(f'{k} تم اضافه الرد المميز ( {text} )\n{k} بـ ( {count} ) جواب رد\n☆',parse_mode=ParseMode.HTML)
   
   if r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:randomFilter:{m.chat.id}{hmshelp}'):
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}')
       return m.reply(f'{k} هذا الرد مو مضاف في قائمة الردود')
     else:
       r.delete(f'{m.text}:randomFilter:{m.chat.id}{hmshelp}')
       r.delete(f'{m.text}:randomfilter:{m.chat.id}{hmshelp}')
       r.delete(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}')
       r.srem(f'{m.chat.id}:RFiltersList:{hmshelp}',m.text)
       return m.reply(f'{k} ابشر مسحت الرد العشوائي ')
       
   
   if r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
     r.delete(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}')
     r.set(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}',m.text)
     return m.reply(f'{k} حلو الحين ارسل اجوبة الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
   
   if r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}') and mod_pls(m.from_user.id,m.chat.id):
     text = r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}')
     r.sadd(f'{text}:randomfilter:{m.chat.id}{hmshelp}', m.text.html)
     return m.reply(f'{k} حلو ضفت هذا الرد\n{k} بس تخلص ارسل تم\nـــــــــــــــــــــــــــــــــــــــــ\n`<USER_ID>` › آيدي المستخدم\n`<USER_NAME>` › اسم المستخدم\n`<USER_USERNAME>` › يوزر المستخدم\n`<USER_MENTION>` › رابط حساب المستخدم\n༄',parse_mode=ParseMode.MARKDOWN)
     
   if text == 'الردود المميزه':
     if not mod_pls(m.from_user.id, m.chat.id):
        return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
      if not r.smembers(f'{m.chat.id}:RFiltersList:{hmshelp}'):
       return m.reply(f'{k} مافيه ردود عشوائيه مضافه')
      else:
       text = 'الردود المميزه:\n'
       count = 1
       for reply in r.smembers(f'{m.chat.id}:RFiltersList:{hmshelp}'):
          rep = reply
          ttt = len(r.smembers(f'{rep}:randomfilter:{m.chat.id}{hmshelp}'))
          text += f'\n{count} - ( {rep} ) ☆ ( {ttt} )'
          count += 1
       text += '\n☆'
       return m.reply(text, disable_web_page_preview=True,parse_mode=ParseMode.HTML)
   
   if text == 'مسح الردود المميزه':
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       if not r.smembers(f'{m.chat.id}:RFiltersList:{hmshelp}'):
         return m.reply(f'{k} مافيه ردود مميزه مضافه')
       else:
         count = 0
         for reply in r.smembers(f'{m.chat.id}:RFiltersList:{hmshelp}'):
            rep = reply
            r.delete(f'{rep}:randomfilter:{m.chat.id}{hmshelp}')
            r.srem(f'{m.chat.id}:RFiltersList:{hmshelp}', rep)
            r.delete(f'{rep}:randomFilter:{m.chat.id}{hmshelp}')
            count += 1
         return m.reply(f'{k} ابشر مسحت ( {count} ) رد مميز ')
            
   if text == 'اضف رد مميز' and not r.get(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}') and not r.get(f'{m.chat.id}:addFilterR2:{m.from_user.id}{hmshelp}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:addFilterR:{m.from_user.id}{hmshelp}',1)
       return m.reply(f'{k} حلو ، ارسل الحين الكلمة الي تبيها')
   
   if text == 'مسح رد مميز' and not r.get(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}'):
     if not mod_pls(m.from_user.id,m.chat.id):
       return m.reply(f'{k} هذا الأمر يخص ( المدير وفوق ) بس')
     else:
       r.set(f'{m.chat.id}:delFilterR:{m.from_user.id}{hmshelp}',1)
       return m.reply(f'{k} تمام عيني\n{k} الحين ارسل الرد عشان امسحه\n☆',parse_mode=ParseMode.HTML)
   
   
     
     
     
