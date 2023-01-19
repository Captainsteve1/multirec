import time
import config
import os.path
from pyrogram import *
from pyrogram.types import *
from urllib.request import urlopen, Request 
from rec import *

newfile = "hi"

tbot = Client("IPTV recorder bot for kids", bot_token=config.bot_token, api_id=config.api_id, api_hash=config.api_hash)

@tbot.on_message(filters.command('rec') & filters.private)
def rip(bot, update):
    message.update.replay_text(text="recording")
    if os.path.exists(newfile) == True:
    msg.edit(text="Recording done")
    bot.send_video(video=newfile, chat_id=update.from_user.id, caption = f'{newfile}'

tbot.run()
