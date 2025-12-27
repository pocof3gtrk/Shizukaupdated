from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from PurviBots import PurviBots
from PurviBots.database import get_served_chats, get_served_users

@PurviBots.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    me = await cli.get_me()
    
    buttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("ʌᴅᴅ ᴍє", url=f"https://t.me/{me.username}?startgroup=true"),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/iamvillain77")
        ]]
    )

    await message.reply_text(
        f"""**🏡 ᴛᴏᴛᴀʟ sᴛᴀᴛs ᴏғ {me.mention} :-**

➻ **ᴄʜᴀᴛs :-** {chats}
➻ **ᴜsᴇʀs :-** {users}""",
        reply_markup=buttons
    )
