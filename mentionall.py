import os, logging, asyncio
import random
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

# ÆkmÉ OÄlum...!!!
emj = ['ð','ð¥°','ð','ð¤©','ð','ð¾','ð¤¡','ð¥³','ð»','ð¼','ð½','ð','ð¸','ð¤´','ðð»','ð¤¶','ð§ââï¸','ð§','ð§ââï¸','ð§ââï¸','ð§','ð§ââï¸','ð§','ð','ð','ð¶','ð¶','ð±','ð­','ð¹','ð°','ð¦','ð»','ð¼','ð¨','ð¯','ð¦','ð®','ð·','ð½','ð¸','ðµ','ð','ð','ð','ð','ð£','ð¥','ð¦','ð','ð¦','ð','ð','ð¹','ð¥','ðº','ð¸','ð¼','ð»','â­ï¸','ð','â¨','â¡ï¸','ð¥','ð','âï¸','ð«','ð','ðº','ð«','ð','â','ð§¸','ð¦','ð©âð¦°','ð®','âï¸','ð','ð¦','ð¨ð»ââï¸','ð¥¶','ð¿','ð','ð','ð','â¥ï¸','ð','ð','ð','ð','ð','ð¤','ð¤','â¡','ð','ð¤¡','ð','ð¥','ð¼','ð¤','â','ð©âð¨','ð§','ð¼','ð','ð¹','ð¥','ð·','ðº','ð¸','ðµï¸','ð»','ð','ð','ð¾','ð±','ð¿','ð','âï¸','ð','ðµ','ð´','ð³','ð²','ðï¸','ðªï¸','âï¸','â','âï¸','ðï¸','ð','ð','ð¤¶','ð©âð¼','ð§','ð§','ð','ðº','ð©âð¦°','ðª','ð¦','ð¢','ð','ð¤','ð£','ð¥','ð¦','ð','ðï¸','ð¦¢','ð¦©','ð¦','ð¬','ð','ð³','ð','ð ','ð¦','ð¡','ð¦','ð¦','ð¦','ð¦','ð','ð¦','ð·ï¸','ð¸ï¸','ð','ð¦','ð¦','ð','ð','ð¾','ð','ð','ð','ð','ð','ð¥­','ð','ð','ð','ð¥','ð','ð¥¥','ð¶ï¸','ð','ð','ð§','ð¥','ð¦','ð§','ð¨','ð¦','ð¥§','ð°','ð®','ð','ð§','ð­','ð¬','ð©','ðº','ð»','ð¥','ð¾','ð·']
# ÆkmÉ OÄlum...!!!

#  gÃ¼zel isimler...!!! 
cumle = ['ÃzÃ¼mlÃ¼ kekim â¨', 'Nar Ã§iÃ§eÄi â¨', 'Papatya ð¼', 'Karanfil â¨', 'GÃ¼l ð¹', 'AyÄ±cÄ±k ð»', 'Mutlu pandam ð¼', 'Ay parem â¨', 'BallÄ± lokmam â¨', 'BebiÅim ð¥°', 'Lale ð·', 'Zambak â', 'Nergis â¨', 'SÃ¼mbÃ¼l âï¸', 'NilÃ¼fer âï¸', 'MenekÅe âï¸', 'Lavanta â¨', 'GÃ¼l pare â¨', 'Reyhan ð·', 'KaktÃ¼s âï¸', 'BÃ¶ÄÃ¼rtlen âï¸', 'Orkide âï¸', 'Manolya â¨', 'AyÃ§iÃ§eÄi â¨', 'Tweety âï¸', 'Star â¨', 'Yonca ð', 'AteÅ bÃ¶ceÄi â¨',]
#  gÃ¼zel isimler...!!!

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**AutoTaggerð¹ð·**, Grup veya kanaldaki neredeyse tÃ¼m Ã¼yelerden bahsedebilirim â\nDaha fazla bilgi iÃ§in **/bilgi**'i tÄ±klayÄ±n.",
                    buttons=(
                      [
                         Button.url('â BENÄ° GRUBA EKLE â ', 'http://t.me/autotagger_bot?startgroup=a')
                      ],
                      [
                         Button.url('ð£ Kanal', 'https://t.me/HerlockBots'),
                         Button.url('ð®Developer', 'https://t.me/tht_herlock'),
                         Button.url('ð Sahib', 'https://t.me/SakirBey1')
                      ]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/bilgi$"))
async def help(event):
  helptext = "**AutoTaggerð¹ð· Bot'un YardÄ±m MenÃ¼sÃ¼**\n\nKomut: /utag \n  Bu komutu, baÅkalarÄ±na bahsetmek istediÄiniz metinle birlikte kullanabilirsiniz. /etag  \n emoji ile etiketleme. \n`Ãrnek: /utag GÃ¼naydÄ±n!`  \nBu komutu yanÄ±t olarak kullanabilirsiniz. herhangi bir mesaj Bot, yanÄ±tlanan iletiye kullanÄ±cÄ±larÄ± etiketleyecek."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('â BENÄ° GRUBA EKLE â', 'http://t.me/autotagger_bot?startgroup=a')
                      ],
                      [
                         Button.url('ð£ Kanal', 'https://t.me/HerlockBots'),
                         Button.url('ð®Developer', 'https://t.me/tht_herlock'),
                         Button.url('ð Sahib', 'https://t.me/SakirBey1')
                      ]
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð§âð§-[{usr.first_name}](tg://user?id={usr.id})\n "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"ð§âð§-[{usr.first_name}](tg://user?id={usr.id})\n "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

# Emoji Modulu (aykhan_s)
@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

#  gÃ¼zel isimler...!!!
@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def nick(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanÄ±labilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("__YalnÄ±zca yÃ¶neticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajlar iÃ§in Ã¼yelerden bahsedemem! (gruba eklemeden Ã¶nce gÃ¶nderilen mesajlar)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Bana bir argÃ¼man ver!__")
  else:
    return await event.respond("__Bir mesajÄ± yanÄ±tlayÄ±n veya baÅkalarÄ±ndan bahsetmem iÃ§in bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Ä°Ålem BaÅarÄ±lÄ± Bir Åekilde Durduruldu â")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

print(">> Bot Ã§alÄ±yor merak etme ð @tht_herlock bilgi alabilirsin <<")
client.run_until_disconnected()
