import asyncio
import importlib
import threading
import time
import requests
from sys import version as pyver
from flask import Flask
from pyrogram import idle, __version__ as pyrover
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PurviBots import LOGGER, PurviBots
from PurviBots.modules import ALL_MODULES
from config import START_LOGGER as LOGGER_GROUP


flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "PurviBots is running!"

def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

def keep_alive():
    while True:
        try:
            requests.get("https://bio-link-ismx.onrender.com")
            LOGGER.info("Pinged host URL successfully")
        except Exception as e:
            LOGGER.error(f"Ping error : {e}")
        time.sleep(300) 

async def send_startup_message():
    try:
        me = await PurviBots.get_me()
        text = f"""
<b>❖ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅</b>

<b>• ʙᴏᴛ :-</b> {me.mention}
<b>• ᴘʟᴜɢɪɴs :-</b> <code>{len(ALL_MODULES)}</code> <b>ʟᴏᴀᴅᴇᴅ</b>
<b>• ᴘʏʀᴏɢʀᴀᴍ :-</b> <code>{pyrover}</code>
<b>• ᴘʏᴛʜᴏɴ :-</b> <code>{pyver.split()[0]}</code>

<b>» ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- <a href="https://t.me/purvibots">ᴘᴜʀᴠɪ-ʙᴏᴛs</a></b>
"""

        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✙ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✙",
                        url=f"https://t.me/{me.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"
                    )
                ]
            ]
        )

        await PurviBots.send_photo(
            chat_id=LOGGER_GROUP,
            photo="https://files.catbox.moe/21ba26.jpg",
            caption=text,
            reply_markup=buttons,        
        )
        LOGGER.info(f"Startup message sent to group {LOGGER_GROUP}")
    except Exception as e:
        LOGGER.error(f"Failed to send startup message: {e}")

async def anony_boot():
    try:
        await PurviBots.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    await send_startup_message()

    successful_loads = 0
    failed_loads = 0
    
    LOGGER.info(f"Loading {len(ALL_MODULES)} modules...")
    
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("PurviBots.modules." + all_module)
            successful_loads += 1
            LOGGER.info(f"✓ {all_module}")
        except Exception as e:
            failed_loads += 1
            LOGGER.error(f"✗ {all_module}: {e}")

    LOGGER.info(f"Modules loaded : {successful_loads} success, {failed_loads} failed")
    LOGGER.info(f"@{PurviBots.username} Started successfully!")
    
    await idle()


if __name__ == "__main__":

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.daemon = True
    keep_alive_thread.start()

    asyncio.get_event_loop().run_until_complete(anony_boot())
    LOGGER.info("Stopping Bot...")
