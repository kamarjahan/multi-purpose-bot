# get file trans must
# credit must [ https://github.com/kamarjahan ]
# copyright by t.me/devourdevils
# all codes are free to use




import os
from pyrogram import Client
from sample_config import Config



devourdevils = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
   plugins=dict(root="programs")
)
devourdevils.run()
