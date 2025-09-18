import random, re, time
from threading import Thread
from pyrogram import *
from AnonXMusic import app
from pyrogram.enums import *
from pyrogram.types import *
from config import *
from helpers.Ranks import *


@app.on_message(filters.text & filters.group, group=31)
def addPluginHandler(c,m):
    k = r.get(f'{hmshelp}:botkey')
    Thread(target=plugin_func,args=(c,m,k)).start()
    
def plugin_func(c,m,k):
   if not r.get(f'{m.chat.id}:enable:{hmshelp}'):
        return
   if r.get(f'{m.from_user.id}:mute:{m.chat.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:mute:{hmshelp}') and not admin_pls(m.from_user.id,m.chat.id):  return
   if r.get(f'{m.from_user.id}:mute:{hmshelp}'):  return 
   
   if r.get(f'{m.chat.id}addCustomG:{m.from_user.id}{hmshelp}'):  return
   if r.get(f'{m.chat.id}:addCustom:{m.from_user.id}{hmshelp}'):  return 
   if r.get(f'{m.chat.id}:delCustom:{m.from_user.id}{hmshelp}') or r.get(f'{m.chat.id}:delCustomG:{m.from_user.id}{hmshelp}'):  return 
   text = m.text
   name = r.get(f'{hmshelp}:BotName') if r.get(f'{hmshelp}:BotName') else 'ميلا'
   if text.startswith(f'{name} '):
      text = text.replace(f'{name} ','')
   if r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}'):
       text = r.get(f'{m.chat.id}:Custom:{m.chat.id}{hmshelp}&text={text}')
   if r.get(f'Custom:{hmshelp}&text={text}'):
       text = r.get(f'Custom:{hmshelp}&text={text}')
   
   if r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}') or r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}'):
     if text == 'الغاء':
       m.reply(f'{k} ابشر ياعيني لغيت كلشي')
       r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{hmshelp}')
       r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}')
       r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}')
       r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}')
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}')
       return 
     
   if text == 'اضف ميزة' or text == 'اضف ميزه':
     if devp_pls(m.from_user.id,m.chat.id):
        r.set(f'{m.from_user.id}:setAddP:{m.chat.id}{hmshelp}',1)
        return m.reply(f'{k} هلا عيني ارسل اسم الميزة الحين')
   
   if r.get(f'{m.from_user.id}:setAddP:{m.chat.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id) and len(m.text.split()) == 1:
      r.delete(f'{m.from_user.id}:setAddP:{m.chat.id}{hmshelp}')
      r.set(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}',m.text)
      return m.reply(f'{k} تمام عيني ارسل نوع الميزة الحين ( صوره,فيديو,متحركه,بصمه,صوت)\n☆')
   
   if text in ['صوره','فيديو','متحركه','بصمه','صوت'] and r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}')
      r.delete(f'{m.from_user.id}:setAddP2:{m.chat.id}{hmshelp}')
      r.set(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}',f'miza={miza}&&type={m.text}')
      return m.reply(f'{k} ارسل يوزر القناة الحين')
   
   if r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}')
      miza += f'&&channel={m.text.replace("@","")}'
      r.delete(f'{m.from_user.id}:setAddP3:{m.chat.id}{hmshelp}')
      r.set(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}', miza)
      return m.reply(f'{k} ارسل الحين ايديات الرسايل العشوائية\n{k} مثال 1 - 100')
   
   if r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
      miza = r.get(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}')
      id1 = int(m.text.split('-')[0])
      id2 = int(m.text.split('-')[1])
      r.delete(f'{m.from_user.id}:setAddP4:{m.chat.id}{hmshelp}')
      miza_name = miza.split('miza=')[1].split('&&')[0]
      miza_type = miza.split('&&type=')[1].split('&&')[0]
      miza_channel = miza.split('&&channel=')[1].split('&&')[0]
      r.set(f'{miza_name}:customPlugin:{hmshelp}', f'type={miza_type}&&channel={miza_channel}&&random={id1}_{id2}')
      r.sadd(f'customPlugins:{hmshelp}', miza_name)
      return m.reply(f'{k} ابشر ضفت الميزة ( {miza_name} )\n{k} نوع الميزة {miza_type}\n{k} قناة الميزة ( @{miza_channel} )')
   
   if text == 'مسح ميزة' or text == 'مسح ميزه':
     if devp_pls(m.from_user.id,m.chat.id):
        r.set(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}',1)
        return m.reply(f'{k} هلا عيني ارسل اسم الميزة الحين')
        
   if r.get(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}') and devp_pls(m.from_user.id,m.chat.id):
     if not r.get(f'{m.text}:customPlugin:{hmshelp}'):
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}')
       return m.reply(f'{k} مافي ميزة بهالأسم')
     else:
       r.srem(f'customPlugins:{hmshelp}', m.text)
       r.delete(f'{m.text}:customPlugin:{hmshelp}')
       r.delete(f'{m.from_user.id}:setDelp:{m.chat.id}{hmshelp}')
       r.delete(f'{m.text}:customPluginD:{hmshelp}{m.chat.id}')
       return m.reply(f'{k} الميزة ( {m.text} ) مسحتها .')
   
   if text == 'المميزات المضافه':
     if devp_pls(m.from_user.id,m.chat.id):
       if not r.smembers(f'customPlugins:{hmshelp}'):
         return m.reply(f'{k} مافي ولا ميزة مضافة')
       else:
         text = 'المميزات المضافه:\n\n'
         count = 1
         for miza in r.smembers(f'customPlugins:{hmshelp}'):
            text += f'{count}) - {miza}\n'
            count += 1
         text += '\n☆'
         return m.reply(text)
   
   if r.get(f'{m.text}:customPlugin:{hmshelp}'):
      if r.get(f'{m.text}:customPluginD:{hmshelp}{m.chat.id}'):
         return
      else:
         miza = r.get(f'{m.text}:customPlugin:{hmshelp}')
         type = miza.split('type=')[1].split('&&')[0]
         channel = miza.split('&&channel=')[1].split('&&')[0]
         random1 = int(miza.split('&&random=')[1].split('_')[0])
         random2 = int(miza.split('&&random=')[1].split('_')[1])
         rand = random.randint(random1,random2)
         if type == 'صوره':
            m.reply_photo(f'https://t.me/{channel}/{rand}')
         
         if type == 'فيديو':
            m.reply_video(f'https://t.me/{channel}/{rand}')
        
         if type == 'متحركه':
            m.reply_animation(f'https://t.me/{channel}/{rand}')
         
         if type == 'بصمه':
            m.reply_voice(f'https://t.me/{channel}/{rand}')
         
         if type == 'صوت':
            m.reply_audio(f'https://t.me/{channel}/{rand}')
   
   if text.startswith('تعطيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if r.get(f'{miza}:customPlugin:{hmshelp}'):
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس') 
        else:
          if r.get(f'{miza}:customPluginD:{hmshelp}{m.chat.id}'):
            return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ميزة {miza} معطله من قبل\n☆')
          else:
            r.set(f'{miza}:customPluginD:{hmshelp}{m.chat.id}',1)
            return m.reply(f'من「 {m.from_user.mention} 」\n{k} ابشر عطلت ميزة {miza}\n☆')
   
   if text.startswith('تفعيل ') and len(text.split()) == 2:
      miza = text.split()[1]
      if r.get(f'{miza}:customPlugin:{hmshelp}'):
        if not owner_pls(m.from_user.id,m.chat.id):
          return m.reply(f'{k} هذا الامر يخص ( المالك وفوق ) بس') 
        else:
          if not r.get(f'{miza}:customPluginD:{hmshelp}{m.chat.id}'):
            return m.reply(f'{k} من「 {m.from_user.mention} 」\n{k} ميزة {miza} مفعله من قبل\n☆')
          else:
            r.delete(f'{miza}:customPluginD:{hmshelp}{m.chat.id}')
            return m.reply(f'من「 {m.from_user.mention} 」\n{k} ابشر فعلت ميزة {miza}\n☆')
   
            
            
          
   
   
   
   
      
   
