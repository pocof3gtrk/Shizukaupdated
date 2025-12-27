from PurviBots import PurviBots as app 
import asyncio
import random
from pyrogram import filters
from pyrogram.enums import ChatType, ChatMemberStatus

spam_chats = []

TAGMES = [ " ** ʜᴇʏ ʙᴀʙʏ ᴋᴀʜᴀ ʜᴏ 🤗** ",
           " ** ᴏʏᴇ sᴏ ɢʏᴇ ᴋʏᴀ ᴏɴʟɪɴᴇ ᴀᴀᴏ 😊** ",
           " ** ᴠᴄ ᴄʜᴀʟᴏ ʙᴀᴛᴇɴ ᴋᴀʀᴛᴇ ʜᴀɪɴ ᴋᴜᴄʜ ᴋᴜᴄʜ 😃** ",
           " ** ᴋʜᴀɴᴀ ᴋʜᴀ ʟɪʏᴇ ᴊɪ..?? 🥲** ",
           " ** ɢʜᴀʀ ᴍᴇ sᴀʙ ᴋᴀɪsᴇ ʜᴀɪɴ ᴊɪ 🥺** ",
           " ** ᴘᴛᴀ ʜᴀɪ ʙᴏʜᴏᴛ ᴍɪss ᴋᴀʀ ʀʜɪ ᴛʜɪ ᴀᴀᴘᴋᴏ 🤭** ",
           " ** ᴏʏᴇ ʜᴀʟ ᴄʜᴀʟ ᴋᴇsᴀ ʜᴀɪ..?? 🤨** ",
           " ** ᴍᴇʀɪ ʙʜɪ sᴇᴛᴛɪɴɢ ᴋᴀʀʙᴀ ᴅᴏɢᴇ..?? 🙂** ",
           " ** ᴀᴀᴘᴋᴀ ɴᴀᴍᴇ ᴋʏᴀ ʜᴀɪ..?? 🥲** ",
           " ** ɴᴀsᴛᴀ ʜᴜᴀ ᴀᴀᴘᴋᴀ..?? 😋** ",
           " ** ᴍᴇʀᴇ ᴋᴏ ᴀᴘɴᴇ ɢʀᴏᴜᴘ ᴍᴇ ᴋɪᴅɴᴀᴘ ᴋʀ ʟᴏ 😍** ",
           " ** ᴀᴀᴘᴋɪ ᴘᴀʀᴛɴᴇʀ ᴀᴀᴘᴋᴏ ᴅʜᴜɴᴅ ʀʜᴇ ʜᴀɪɴ ᴊʟᴅɪ ᴏɴʟɪɴᴇ ᴀʏɪᴀᴇ 😅** ",
           " ** ᴍᴇʀᴇ sᴇ ᴅᴏsᴛɪ ᴋʀᴏɢᴇ..?? 🤔** ",
           " ** ᴇᴅʜᴀʀ ᴅᴇᴋʜᴏ ᴋʏᴀ ʜᴀɪ @ONE_WAS_SIGMA ...😘** ",
           " ** ʙᴀʙᴜ ʏᴇ ᴅᴇᴋʜᴏ ᴀʟᴘʜᴀ ᴋᴀ ᴀᴅᴅᴀ @Oye_Careless... 😎** ",
           " ** sᴏɴᴇ ᴄʜᴀʟ ɢʏᴇ ᴋʏᴀ 🙄** ",
           " ** ᴇᴋ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ ᴘʟss 😕** ",
           " ** ᴀᴀᴘ ᴋᴀʜᴀ sᴇ ʜᴏ..?? 🙃** ",
           " ** ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ 😛** ",
           " ** ʜᴇʟʟᴏ ʙᴀʙʏ ᴋᴋʀʜ..? 🤔** ",
           " ** ᴅᴏ ʏᴏᴜ ᴋɴᴏᴡ ᴡʜᴏ ɪs ᴍʏ ᴏᴡɴᴇʀ.? ☺️** ",
           " ** ᴄʜʟᴏ ᴋᴜᴄʜ ɢᴀᴍᴇ ᴋʜᴇʟᴛᴇ ʜᴀɪɴ.🤗** ",
           " ** ᴀᴜʀ ʙᴀᴛᴀᴏ ᴋᴀɪsᴇ ʜᴏ ʙᴀʙʏ 😇** ",
           " ** ᴛᴜᴍʜᴀʀɪ ᴍᴜᴍᴍʏ ᴋʏᴀ ᴋᴀʀ ʀᴀʜɪ ʜᴀɪ 🤭** ",
           " ** ᴍᴇʀᴇ sᴇ ʙᴀᴛ ɴᴏɪ ᴋʀᴏɢᴇ 🥺** ",
           " ** ᴏʏᴇ ᴘᴀɢᴀʟ ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ 😶** ",
           " ** ᴀᴀᴊ ʜᴏʟɪᴅᴀʏ ʜᴀɪ ᴋʏᴀ sᴄʜᴏᴏʟ ᴍᴇ..?? 🤔** ",
           " ** ᴏʏᴇ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 😜** ",
           " ** sᴜɴᴏ ᴇᴋ ᴋᴀᴍ ʜᴀɪ ᴛᴜᴍsᴇ 🙂** ",
           " ** ᴋᴏɪ sᴏɴɢ ᴘʟᴀʏ ᴋʀᴏ ɴᴀ 😪** ",
           " ** ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜ ☺** ",
           " ** ᴍᴇʀᴀ ʙᴀʙᴜ ɴᴇ ᴛʜᴀɴᴀ ᴋʜᴀʏᴀ ᴋʏᴀ..? 🙊** ",
           " ** sᴛᴜᴅʏ ᴄᴏᴍᴘʟᴇᴛᴇ ʜᴜᴀ?? 😺** ",
           " ** ʙᴏʟᴏ ɴᴀ ᴋᴜᴄʜ ʏʀʀ 🥲** ",
           " ** sᴏɴᴀʟɪ ᴋᴏɴ ʜᴀɪ...?? 😅** ",
           " ** ᴛᴜᴍʜᴀʀɪ ᴇᴋ ᴘɪᴄ ᴍɪʟᴇɢɪ..? 😅** ",
           " ** ᴍᴜᴍᴍʏ ᴀᴀ ɢʏɪ ᴋʏᴀ 😆** ",
           " ** ᴏʀ ʙᴀᴛᴀᴏ ʙʜᴀʙʜɪ ᴋᴀɪsɪ ʜᴀɪ 😉** ",
           " ** ɪ ʟᴏᴠᴇ ʏᴏᴜ 💚** ",
           " ** ᴅᴏ ʏᴏᴜ ʟᴏᴠᴇ ᴍᴇ..? 👀** ",
           " ** ʀᴀᴋʜɪ ᴋᴀʙ ʙᴀɴᴅ ʀᴀʜɪ ʜᴏ..?? 🙉** ",
           " ** ᴇᴋ sᴏɴɢ sᴜɴᴀᴜ..? 😹** ",
           " ** ᴏɴʟɪɴᴇ ᴀᴀ ᴊᴀ ʀᴇ sᴏɴɢ sᴜɴᴀ ʀᴀʜɪ ʜᴜ 😻** ",
           " ** ɪɴsᴛᴀɢʀᴀᴍ ᴄʜᴀʟᴀᴛᴇ ʜᴏ..?? 🙃** ",
           " ** ᴡʜᴀᴛsᴀᴘᴘ ɴᴜᴍʙᴇʀ ᴅᴏɢᴇ ᴀᴘɴᴀ ᴛᴜᴍ..? 😕** ",
           " ** ᴛᴜᴍʜᴇ ᴋᴏɴ sᴀ ᴍᴜsɪᴄ sᴜɴɴᴀ ᴘᴀsᴀɴᴅ ʜᴀɪ..? 🙃** ",
           " ** sᴀʀᴀ ᴋᴀᴍ ᴋʜᴀᴛᴀᴍ ʜᴏ ɢʏᴀ ᴀᴀᴘᴋᴀ..? 🙃** ",
           " ** ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ 😊** ",
           " ** sᴜɴᴏ ɴᴀ 🧐** ",
           " ** ᴍᴇʀᴀ ᴇᴋ ᴋᴀᴀᴍ ᴋᴀʀ ᴅᴏɢᴇ..? ♥️** ",
           " ** ʙʏ ᴛᴀᴛᴀ ᴍᴀᴛ ʙᴀᴀᴛ ᴋᴀʀɴᴀ ᴀᴀᴊ ᴋᴇ ʙᴀᴅ 😠** ",
           " ** ᴍᴏᴍ ᴅᴀᴅ ᴋᴀɪsᴇ ʜᴀɪɴ..? ❤** ",
           " ** ᴋʏᴀ ʜᴜᴀ..? 🤔** ",
           " ** ʙᴏʜᴏᴛ ʏᴀᴀᴅ ᴀᴀ ʀʜɪ ʜᴀɪ 😒** ",
           " ** ʙʜᴜʟ ɢʏᴇ ᴍᴜᴊʜᴇ 😏** ",
           " ** ᴊᴜᴛʜ ɴʜɪ ʙᴏʟɴᴀ ᴄʜᴀʜɪʏᴇ 🤐** ",
           " ** ᴋʜᴀ ʟᴏ ʙʜᴀᴡ ᴍᴀᴛ ᴋʀᴏ ʙᴀᴀᴛ 😒** ",
           " ** ᴋʏᴀ ʜᴜᴀ 😮** "
           " ** ʜɪɪ ʜᴏɪ ʜᴇʟʟᴏ 👀** ",
           " ** ᴀᴀᴘᴋᴇ ᴊᴀɪsᴀ ᴅᴏsᴛ ʜᴏ sᴀᴛʜ ᴍᴇ ғɪʀ ɢᴜᴍ ᴋɪs ʙᴀᴀᴛ ᴋᴀ 🙈** ",
           " ** ᴀᴀᴊ ᴍᴇ sᴀᴅ ʜᴏᴏɴ ☹️** ",
           " ** ᴍᴜsᴊʜsᴇ ʙʜɪ ʙᴀᴀᴛ ᴋᴀʀ ʟᴏ ɴᴀ 🥺** ",
           " ** ᴋʏᴀ ᴋᴀʀ ʀᴀʜᴇ ʜᴏ 👀** ",
           " ** ᴋʏᴀ ʜᴀʟ ᴄʜᴀʟ ʜᴀɪ 🙂** ",
           " ** ᴋᴀʜᴀ sᴇ ʜᴏ ᴀᴀᴘ..?🤔** ",
           " ** ᴄʜᴀᴛᴛɪɴɢ ᴋᴀʀ ʟᴏ ɴᴀ..🥺** ",
           " ** ᴍᴇ ᴍᴀsᴏᴏᴍ ʜᴜ ɴᴀ 🥺** ",
           " ** ᴋᴀʟ ᴍᴀᴊᴀ ᴀʏᴀ ᴛʜᴀ ɴᴀ 😅** ",
           " ** ɢʀᴏᴜᴘ ᴍᴇ ʙᴀᴀᴛ ᴋʏᴜ ɴᴀʜɪ ᴋᴀʀᴛᴇ ʜᴏ 😕** ",
           " ** ᴀᴀᴘ ʀᴇʟᴀᴛɪᴏɴsʜɪᴘ ᴍᴇ ʜᴏ..? 👀** ",
           " ** ᴋɪᴛɴᴀ ᴄʜᴜᴘ ʀᴀʜᴛᴇ ʜᴏ ʏʀʀ 😼** ",
           " ** ᴀᴀᴘᴋᴏ ɢᴀɴᴀ ɢᴀɴᴇ ᴀᴀᴛᴀ ʜᴀɪ..? 😸** ",
           " ** ɢʜᴜᴍɴᴇ ᴄʜᴀʟᴏɢᴇ..?? 🙈** ",
           " ** ᴋʜᴜs ʀᴀʜᴀ ᴋᴀʀᴏ 🤞** ",
           " ** ʜᴀᴍ ᴅᴏsᴛ ʙᴀɴ sᴀᴋᴛᴇ ʜᴀɪ...? 🥰** ",
           " ** ᴋᴜᴄʜ ʙᴏʟ ᴋʏᴜ ɴʜɪ ʀᴀʜᴇ ʜᴏ.. 🥺** ",
           " ** ᴋᴜᴄʜ ᴍᴇᴍʙᴇʀs ᴀᴅᴅ ᴋᴀʀ ᴅᴏ 🥲** ",
           " ** sɪɴɢʟᴇ ʜᴏ ʏᴀ ᴍɪɴɢʟᴇ 😉** ",
           " ** ᴀᴀᴏ ᴘᴀʀᴛʏ ᴋᴀʀᴛᴇ ʜᴀɪɴ 🥳** ",
           " ** ʙɪᴏ ᴍᴇ ʟɪɴᴋ ʜᴀɪ ᴊᴏɪɴ ᴋᴀʀ ʟᴏ 🧐** ",
           " ** ᴍᴜᴊʜᴇ ʙʜᴜʟ ɢʏᴇ ᴋʏᴀ 🥺** ",
           " ** ʏᴀʜᴀ ᴀᴀ ᴊᴀᴏ @ALPHA_SAYS ᴍᴀsᴛɪ ᴋᴀʀᴇɴɢᴇ 🤭** ",
           " ** ᴛʀᴜᴛʜ ᴀɴᴅ ᴅᴀʀᴇ ᴋʜᴇʟᴏɢᴇ..? 😊** ",
           " ** ᴀᴀᴊ ᴍᴜᴍᴍʏ ɴᴇ ᴅᴀᴛᴀ ʏʀʀ 🥺** ",
           " ** ᴊᴏɪɴ ᴋᴀʀ ʟᴏ @Purvi_Updates 🤗** ",
           " ** ᴇᴋ ᴅɪʟ ʜᴀɪ ᴇᴋ ᴅɪʟ ʜɪ ᴛᴏ ʜᴀɪ 😗** ",
           " ** ᴛᴜᴍʜᴀʀᴇ ᴅᴏsᴛ ᴋᴀʜᴀ ɢʏᴇ 🥺** ",
           " ** ᴍʏ ᴄᴜᴛᴇ ᴏᴡɴᴇʀ @PurviBots 🥰** ",
           " ** ᴋᴀʜᴀ ᴋʜᴏʏᴇ ʜᴏ ᴊᴀᴀɴ 😜** ",
           " ** ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ ʙʜᴜᴛ ʀᴀᴛ ʜᴏ ɢʏɪ 🥰** ",
           ]


@app.on_message(filters.command(["rtag", "tagall"], prefixes=["/", "@", "#"]))
async def mentionall(client, message):

    chat_id = message.chat.id

    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("**⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.**")

    is_admin = False
    try:
        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
            is_admin = True
    except:
        pass

    if not is_admin:
        return await message.reply("**⬤ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ.**")

    await message.delete()

    if chat_id in spam_chats:
        return await client.send_message(chat_id, "**⬤ ᴛᴀɢɢɪɴɢ ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ… ᴜsᴇ /tagoff.**")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""

    async for usr in client.get_chat_members(chat_id):

        if chat_id not in spam_chats:
            break

        if usr.user.is_bot:
            continue

        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(TAGMES)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""

    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["rstop", "tagstop", "tagoff"]))
async def cancel_spam(client, message):

    chat_id = message.chat.id

    is_admin = False
    try:
        member = await client.get_chat_member(chat_id, message.from_user.id)
        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
            is_admin = True
    except:
        pass

    if not is_admin:
        return await message.reply("**⬤ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ sᴛᴏᴘ ʙᴀʙʏ.**")

    await message.delete()

    if chat_id not in spam_chats:
        return await client.send_message(chat_id, "**⬤ ɴᴏ ᴛᴀɢɢɪɴɢ ɪs ʀᴜɴɴɪɴɢ ʙᴀʙʏ.**")

    try:
        spam_chats.remove(chat_id)
    except:
        pass

    return await client.send_message(chat_id, "**⬤ ᴛᴀɢɢɪɴɢ sᴛᴏᴘᴘᴇᴅ ʙᴀʙʏ.**")
