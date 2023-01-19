import time
import config
from pyrogram import *
from pyrogram.types import *
from urllib.request import urlopen, Request 
from rec import *


tbot = Client("IPTV recorder bot for kids", bot_token=config.bt, api_id=config.api_id, api_hash=config.api_hash)

@tbot.on_message(filters.command('start') & filters.private)
def multirec():
    
