import asyncio
import random
from config import OWNER_ID, IMG
from config import EVENTS_LOGGER as LOGGER_GROUP_ID
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from PurviBots import PurviBots
from PurviBots.database import add_served_chat, add_served_user, remove_served_chat
from PurviBots.purvi.buttons import ABOUT_BUTTON, HELP_BUTTON, ALPHA_BTNS, ALPHA_BACK, HELP_BACK, STBUTTON
from PurviBots.purvi.helper import HELP_BASIC, HELP_MAIN, HELP_ABOUT, START, HELP_CHAT, HELP_WEL, HELP_TAG, HELP_INFO, HELP_RANK

@PurviBots.on_cmd(["start"])
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        user = m.from_user
        user_id = user.id
        username = f"@{user.username}" if user.username else "No Username"
        
        log_msg = f"""**✦ ηєᴡ ᴜsєʀ sᴛᴧʀᴛєᴅ ᴛʜє ʙσᴛ**

**➻ ᴜsєʀ :** [{user.first_name}](tg://user?id={user_id})
**➻ ᴜsєʀɴᴀᴍᴇ :** {username}
**➻ ɪᴅ :** `{user_id}`"""
        
        await PurviBots.send_message(LOGGER_GROUP_ID, log_msg)
        
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=START,
            reply_markup=InlineKeyboardMarkup(STBUTTON),
        )
        await add_served_user(user_id)


@PurviBots.on_message(filters.new_chat_members)
async def on_new_chat_members(client: PurviBots, message: Message):
    bot_id = (await client.get_me()).id
    new_members = message.new_chat_members

    if bot_id not in [user.id for user in new_members]:
        return

    chat_id = message.chat.id
    chat_title = message.chat.title or "Private Chat"
    chat_username = message.chat.username
    added_by = message.from_user.mention if message.from_user else "Unknown User"
    
    try:
        chat_members_count = await client.get_chat_members_count(chat_id)
    except Exception:
        chat_members_count = "Unknown"

    try:
        invite_link = await client.export_chat_invite_link(chat_id)
    except Exception:
        invite_link = "https://t.me/iamvillain77"

    await add_served_chat(chat_id)

    await message.reply_photo(
        photo=random.choice(IMG),
        caption=START,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "✙ ᴀᴅᴅ ᴍᴇ ✙",
                    url=f"https://t.me/{PurviBots.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users+ban_users"
                ),
                InlineKeyboardButton("⌯ sᴜᴘᴘᴏʀᴛ ⌯", url="https://t.me/iamvillain77")
            ]
        ])
    )

    log_msg = (
        f"**✦ ʙᴏᴛ #ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɢʀᴏᴜᴘ**\n\n"
        f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :-** {chat_title}\n"
        f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :-** {chat_id}\n"
        f"**⚘ ᴜsᴇʀɴᴀᴍᴇ :-** @{chat_username if chat_username else 'N/A'}\n"
        f"**⚘ ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs :-** {chat_members_count}\n"
        f"**⚘ ɢʀᴏᴜᴘ ʟɪɴᴋ :-** [ʟɪɴᴋ]({invite_link})\n"
        f"**⚘ ᴀᴅᴅᴇᴅ ʙʏ :-** {added_by}"
    )

    await client.send_photo(
        LOGGER_GROUP_ID,
        photo=random.choice(IMG),
        caption=log_msg,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ɢʀᴏᴜᴘ ʟɪɴᴋ", url=invite_link)]
        ])
    )    

@PurviBots.on_message(filters.left_chat_member)
async def on_left_chat_member(client: PurviBots, message: Message):
    bot_id = (await client.get_me()).id

    if message.left_chat_member.id != bot_id:
        return

    chat_id = message.chat.id
    chat_title = message.chat.title
    remove_by = message.from_user.mention if message.from_user else "Unknown User"

    
    try:
        await remove_served_chat(chat_id)
    except:
        pass  

    left_msg = (
        f"**✦ ʙᴏᴛ #ʟᴇғᴛ ᴀ ɢʀᴏᴜᴘ**\n\n"
        f"**⚘ ɢʀᴏᴜᴘ ɴᴀᴍᴇ :-** {chat_title}\n"
        f"**⚘ ɢʀᴏᴜᴘ ɪᴅ :-** {chat_id}\n"
        f"**⚘ ʀᴇᴍᴏᴠᴇᴅ ʙʏ :-** {remove_by}"
    )

    group_link = f"https://t.me/{message.chat.username}" if message.chat.username else "https://t.me/iamvillain77"
    
    await client.send_photo(
        LOGGER_GROUP_ID,
        photo=random.choice(IMG),
        caption=left_msg,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ", url=group_link)]
        ])
    )
@PurviBots.on_callback_query(filters.regex('back'))
async def back_to_menu(client, callback_query):
    
    
    await callback_query.message.edit_text(
        text=START,
        reply_markup=InlineKeyboardMarkup(STBUTTON),
    )

@PurviBots.on_callback_query(filters.regex('ABOUT'))
async def about_section(client, callback_query):
    about_text = HELP_ABOUT
    
    keyboard = InlineKeyboardMarkup(ABOUT_BUTTON) 
    
    await callback_query.answer()
    await callback_query.message.edit_text(about_text, reply_markup=keyboard)


@PurviBots.on_callback_query(filters.regex('ALPHA_WEL'))
async def help_main(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_WEL,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )


@PurviBots.on_callback_query(filters.regex('ALPHA_MAIN'))
async def alpha_main(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_MAIN,
        reply_markup=InlineKeyboardMarkup(ALPHA_BTNS)
    )

@PurviBots.on_callback_query(filters.regex('ALPHA_BASIC'))
async def alpha_basic(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_BASIC,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )

@PurviBots.on_callback_query(filters.regex('ALPHA_CHAT'))
async def alpha_auth(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_CHAT,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )

@PurviBots.on_callback_query(filters.regex('ALPHA_TAG'))
async def alpha_del(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_TAG,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )

@PurviBots.on_callback_query(filters.regex('ALPHA_INFO'))
async def alpha_del(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_INFO,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )

@PurviBots.on_callback_query(filters.regex('ALPHA_RANK'))
async def alpha_del(client, callback_query):
    await callback_query.message.edit_caption(
        caption=HELP_RANK,
        reply_markup=InlineKeyboardMarkup(ALPHA_BACK)
    )
    
