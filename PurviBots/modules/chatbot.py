from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
from pyrogram.enums import ChatAction, ChatMemberStatus
from PurviBots import PurviBots as app
import random, asyncio, time
from PurviBots.database import is_SonaliChat_enabled, enable_SonaliChat, disable_SonaliChat, SonaliChat_api, STICKERS

USER_COOLDOWN = {} 
COOLDOWN_TIME = 30 

@app.on_message(filters.sticker & ~filters.bot)
async def sticker_auto_reply(_, message: Message):

    chat = message.chat

    if chat.type != "private":
        if not await is_SonaliChat_enabled(chat.id):
            return

    BOT_ID = (await app.get_me()).id

    if message.reply_to_message:
        if message.reply_to_message.from_user.id != BOT_ID:
            return

    if not STICKERS:
        return

    await app.send_chat_action(chat.id, ChatAction.CHOOSE_STICKER)
    await asyncio.sleep(2)

    random_sticker = random.choice(STICKERS)

    try:
        await message.reply_sticker(random_sticker)
    except Exception as e:
        print("Sticker reply error:", e)

async def is_admins(client, chat_id: int, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
    except:
        return False


async def text_filter(_, __, m: Message):
    return (
        bool(m.text)
        and len(m.text) <= 69
        and not m.text.startswith(("!", "/"))
        and (not m.reply_to_message or (m.reply_to_message.from_user and m.reply_to_message.from_user.id == m._client.me.id))
        and not (m.mentioned and (m.text.startswith("!") or m.text.startswith("/")))
    )

SonaliChat_filter = filters.create(text_filter)


@app.on_message(
    (filters.text & filters.group & SonaliChat_filter & ~filters.regex(r"^[/!]"))
    & ~filters.bot
)
async def SonaliChat(_, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    now = time.time()

    if not await is_SonaliChat_enabled(chat_id):
        return

    
    if message.entities:
        for ent in message.entities:
            if ent.type in ("mention", "text_mention"):
                return

    
    if message.reply_to_message and message.reply_to_message.from_user:
        if message.reply_to_message.from_user.id == app.me.id:
            pass
        else:
            
            return
    else:
        last_time = USER_COOLDOWN.get(user_id, 0)
        if now - last_time < COOLDOWN_TIME:
            return

    USER_COOLDOWN[user_id] = now

    await app.send_chat_action(chat_id, ChatAction.TYPING)
    reply = SonaliChat_api.ask_question(message.text)
    await message.reply_text(
        reply or "❖ ᴄʜᴀᴛʙᴏᴛ ᴇʀʀᴏʀ. ᴄᴏɴᴛᴀᴄᴛ @iamvillain77."
    )



@app.on_message(filters.private & filters.text & ~filters.bot & ~filters.regex(r"^[/!]"))
async def SonaliChat_pm(_, message: Message):
    await app.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = SonaliChat_api.ask_question(message.text)
    await message.reply_text(reply or "❖ ᴄʜᴀᴛʙᴏᴛ ᴇʀʀᴏʀ. ᴄᴏɴᴛᴀᴄᴛ @iamvillain77.")


@app.on_message(filters.command("chatbot") & filters.group & ~filters.bot)
async def SonaliChat_toggle(_, message: Message):
    chat_id = message.chat.id

    if not await is_admins(_, chat_id, message.from_user.id):
        await message.reply_text("❖ **ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ !!**")
        return

    chat_title = message.chat.title
    status = await is_SonaliChat_enabled(chat_id)
    status_text = "ᴇɴᴀʙʟᴇᴅ" if status else "ᴅɪꜱᴀʙʟᴇᴅ"

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ᴇɴᴀʙʟᴇ", callback_data="SonaliChat_enable"),
            InlineKeyboardButton("ᴅɪꜱᴀʙʟᴇ", callback_data="SonaliChat_disable")
        ]
    ])

    await message.reply_text(
        f"❖ ᴄᴜʀʀᴇɴᴛʟʏ ᴄʜᴀᴛʙᴏᴛ ɪꜱ **{status_text}** ɪɴ **{chat_title}**.",
        reply_markup=keyboard
    )


@app.on_callback_query(filters.regex("SonaliChat_"))
async def SonaliChat_button_toggle(_, query):
    chat_id = query.message.chat.id
    user = query.from_user

    if not await is_admins(_, chat_id, user.id):
        await query.answer("❖ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ !!", show_alert=True)
        return

    if query.data == "SonaliChat_enable":
        if await is_SonaliChat_enabled(chat_id):
            return await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.", show_alert=True)

        await enable_SonaliChat(chat_id)
        await query.message.edit_text(f"❖ ᴄʜᴀᴛʙᴏᴛ **ᴇɴᴀʙʟᴇᴅ** ʙʏ {user.mention}.")
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ !!")

    else:
        if not await is_SonaliChat_enabled(chat_id):
            return await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ.", show_alert=True)

        await disable_SonaliChat(chat_id)
        await query.message.edit_text(f"❖ ᴄʜᴀᴛʙᴏᴛ **ᴅɪꜱᴀʙʟᴇᴅ** ʙʏ {user.mention}.")
        await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴅɪꜱᴀʙʟᴇᴅ !!")
