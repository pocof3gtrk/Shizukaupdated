import asyncio
import time
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from PurviBots import PurviBots
from PurviBots.database import get_served_chats, get_served_users

IS_BROADCASTING = False
OWNER_ID = 7473021518

@PurviBots.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_message(client: PurviBots, message: Message):
    global IS_BROADCASTING
    
    if IS_BROADCASTING:
        return await message.reply_text("🚫 **ʙʀᴏᴀᴅᴄᴀsᴛ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴘʀᴏɢʀᴇss...**")
    
    
    if message.reply_to_message:
        
        broadcast_message = message.reply_to_message
        use_forward = True
    else:
    
        if len(message.command) < 2:
            return await message.reply_text("**» ᴜsᴀɢᴇ :-** `/broadcast` **ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ**")
        query = message.text.split(None, 1)[1]
        broadcast_message = query
        use_forward = False
    
    IS_BROADCASTING = True
    start_time = time.time()

    all_chats = await get_served_chats()
    all_users = await get_served_users()
    
    total_targets = len(all_chats) + len(all_users)
    sent_chats = 0
    sent_users = 0
    failed_chats = 0
    failed_users = 0
    
    progress_msg = await message.reply_text(f"📢 **ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴀʀᴛᴇᴅ...**")
    
    
    for chat in all_chats:
        if not IS_BROADCASTING:
            break
            
        chat_id = chat["chat_id"]
        try:
            if use_forward:
                
                await broadcast_message.forward(chat_id)
            else:
                
                await client.send_message(chat_id, text=broadcast_message)
            sent_chats += 1
            await asyncio.sleep(0.1)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except Exception:
            failed_chats += 1
            continue
    
    
    for user in all_users:
        if not IS_BROADCASTING:
            break
            
        user_id = user["user_id"]
        try:
            if use_forward:
                
                await broadcast_message.forward(user_id)
            else:
                
                await client.send_message(user_id, text=broadcast_message)
            sent_users += 1
            await asyncio.sleep(0.1)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except Exception:
            failed_users += 1
            continue
    
    time_taken = int(time.time() - start_time)
    total_sent = sent_chats + sent_users
    total_failed = failed_chats + failed_users
    
    if IS_BROADCASTING:
        result_text = f"""
✅ **ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ !!**

🏘 **ᴄʜᴀᴛs :-**
   **├ ✅ sᴜᴄᴄᴇss :-** `{sent_chats}`
   **└ ❌ ғᴀɪʟᴇᴅ :-** `{failed_chats}`

👤 **ᴜsᴇʀs :-**
   **├ ✅ sᴜᴄᴄᴇss :-** `{sent_users}`
   **└ ❌ ғᴀɪʟᴇᴅ :-** `{failed_users}`

📊 **ᴛᴏᴛᴀʟ :-**
   **├ ✅ sᴜᴄᴄᴇss :-** `{total_sent}`
   **└ ❌ ғᴀɪʟᴇᴅ :-** `{total_failed}`

⏱ **ᴛɪᴍᴇ ᴛᴀᴋᴇɴ :-** `{time_taken}` seconds
"""
        await progress_msg.edit_text(result_text)
    else:
        await progress_msg.edit_text("🛑 **ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴏᴘᴘᴇᴅ !!**")
    
    IS_BROADCASTING = False

@PurviBots.on_message(filters.command("stopbc") & filters.user(OWNER_ID))
async def stop_broadcast(client: PurviBots, message: Message):
    global IS_BROADCASTING
    if IS_BROADCASTING:
        IS_BROADCASTING = False
        await message.reply_text("🛑 **ʙʀᴏᴀᴅᴄᴀsᴛ sᴛᴏᴘᴘᴇᴅ !!**")
    else:
        await message.reply_text("ℹ️ **ɴᴏ ʙʀᴏᴀᴅᴄᴀsᴛ ʀᴜɴɴɪɴɢ.**")
