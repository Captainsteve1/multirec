import time
import config
import os.path
from pyrogram import *
from pyrogram.types import *
from urllib.request import urlopen, Request 
from imp import *

tbot = Client("IPTV recorder bot for kids", bot_token=config.bot_token, api_id=config.api_id, api_hash=config.api_hash)

@tbot.on_message(filters.command('rec') & filters.private)
def mutirec(client, message):
    multirec(client, message)
    message.reply_text(text="recording")

newfile = multirec(client, message, channel, url, title, lang, s, s2)

if os.path.exists(newfile) == True:
   msg.edit(text="Recording done")
   bot.send_video(video=newfile, chat_id=update.from_user.id, caption = f'{newfile}')

print("______-----_____")
print("Bot Starting Up!")
print("Bot Started Up!")
tbot.run()
