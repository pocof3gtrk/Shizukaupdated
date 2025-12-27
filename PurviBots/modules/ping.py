import random
import asyncio
from datetime import datetime
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from PurviBots import PurviBots as app


IMG = [
    "https://files.catbox.moe/6qzh5y.jpg",
    "https://files.catbox.moe/9fqgen.jpg",
    "https://files.catbox.moe/et8fz6.jpg",
    "https://files.catbox.moe/ow4v71.jpg",
    "https://files.catbox.moe/nqzk5h.jpg"
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="✙ ʌᴅᴅ ϻє ✙", 
            url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"
        ),
        InlineKeyboardButton(
            text="⌯ 𝛅ᴜᴘᴘᴏʀᴛ ⌯", 
            url=f"https://t.me/iamvillain77"
        ),
    ],
]

start_time = datetime.now()

@app.on_message(filters.command("ping"))
async def ping(client, message: Message):
    start = datetime.now()
    t = "**» ᴘɪηɢɪηɢ..😱**"
    txxt = await message.reply(t)
    await asyncio.sleep(0.25)
    await txxt.edit_text("**» ᴘɪηɢɪηɢ...❤️‍🔥**")
    await asyncio.sleep(0.35)
    await txxt.delete()
    end = datetime.now()
    ms = (end-start).microseconds / 1000
    uptime = datetime.now() - start_time
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    await message.reply_photo(
        photo=random.choice(IMG),
        caption=f"**ʜєʏ ʙᴧʙʏ !!**\n**[{app.name}](t.me/{app.username}) ɪꜱ ᴧʟɪᴠє 🥀 ᴧηᴅ ᴡσʀᴋɪηɢ ꜰɪηє ᴡɪᴛʜ**\n\n**➥ ᴘσηɢ :** `{ms}` ms\n**➥ ᴜᴘᴛɪϻє :** `{hours}`ʜ:`{minutes}`ᴍ:`{seconds}`s\n\n**✦ 𝐏σᴡєʀєᴅ вʏ » [ꪜ 𝛊 ɭ ɭ ᧘ 𝛊 𝛈](t.me/iamakki001)**",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
