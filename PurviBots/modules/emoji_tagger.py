import asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
import random

from PurviBots import PurviBots as Client

SPAM_CHATS = []

EMOJI = [
    "😊","😍","😘","🥰","😻","💖","💕","💓","💗","💞","💟",
    "🌸","🌺","🌷","🌹","💐","🌼","🌻","🍀","🍁","🍂","🍃",
    "🌿","🌱","🌴","🌳","🌲","🌵","🦋","🐦","🐾","🌞","🌝",
    "🌛","🌜","🌕","🌙","🌟","🌠","🌌","✨","💫","⭐️","☀️",
    "🌤","⛅️","🌥","🌦","🌧","🌨","🌩","⛈","🌪","🌫","🌬",
    "☔️","❄️","🌈","⛄️","🌊","🌋","🏞","🏔","🌏","🌍","🌎",
    "🎆","🎇","🎑","🏵","🏅","🎖","🎗","🎐","🎀","🎁","🎊",
    "🎉","🦢","🦚","🦜","🕊","🐇","🐚","🌠","🌉","🌃","🌌"
]


async def is_admin(client, chat_id, user_id):
    try:
        admins = [
            admin.user.id async for admin in client.get_chat_members(
                chat_id, filter=ChatMembersFilter.ADMINISTRATORS
            )
        ]
        return user_id in admins
    except:
        return False


@Client.on_message(filters.command("etag"))
async def etag_cmd(client, message):

    try:
        await message.delete()
    except:
        pass

    if message.chat.type == "private":
        return await message.reply_text("**⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs!**")

    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("**⬤ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ**")

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text("**⬤ ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ… ᴜsᴇ /estop ᴛᴏ sᴛᴏᴘ.**")

    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("**» ᴜsᴇ :-** `/etag hello friends` **ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ.**")

    SPAM_CHATS.append(message.chat.id)

    text = (
        message.reply_to_message.text
        if message.reply_to_message
        else message.text.split(None, 1)[1]
    )

    try:
        buffer = ""
        count = 0

        async for m in client.get_chat_members(message.chat.id):

            if message.chat.id not in SPAM_CHATS:
                break

            if m.user.is_bot or m.user.is_deleted:
                continue

            count += 1
            buffer += f"[{random.choice(EMOJI)}](tg://user?id={m.user.id}) "

            if count == 7:
                await message.reply_text(f"**{text}**\n\n{buffer}")
                await asyncio.sleep(1)
                buffer = ""
                count = 0

        if buffer:
            await message.reply_text(f"**{text}**\n\n{buffer}")

    except FloodWait as e:
        await asyncio.sleep(e.value)

    finally:
        if message.chat.id in SPAM_CHATS:
            SPAM_CHATS.remove(message.chat.id)


@Client.on_message(filters.command("estop"))
async def estop_cmd(client, message):

    try:
        await message.delete()
    except:
        pass

    if message.chat.type == "private":
        return await message.reply_text("**⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ᴡᴏʀᴋs ɪɴ ɢʀᴏᴜᴘs!**")

    if not await is_admin(client, message.chat.id, message.from_user.id):
        return await message.reply_text("**⬤ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ**")

    if message.chat.id in SPAM_CHATS:
        SPAM_CHATS.remove(message.chat.id)
        return await message.reply_text("**⬤ ᴇᴍᴏᴊɪ ᴛᴀɢ sᴛᴏᴘ sᴜᴄᴄᴇssғᴜʟʟʏ!**")

    await message.reply_text("**⬤ ɴᴏ ᴛᴀɢ ᴘʀᴏᴄᴇss ɪs ʀᴜɴɴɪɴɢ.**")
