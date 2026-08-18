from motor.motor_asyncio import AsyncIOMotorClient
import config

ChatBot = AsyncIOMotorClient(config.MONGO_URL)
db = ChatBot["ChatBot"]
chatsdb = db["chats"]    

async def is_SonaliChat_enabled(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    return chat is None

async def enable_SonaliChat(chat_id: int):
    await chatsdb.delete_one({"chat_id": chat_id})

async def disable_SonaliChat(chat_id: int):
    if not await chatsdb.find_one({"chat_id": chat_id}):
        await chatsdb.insert_one({"chat_id": chat_id})

async def get_enabled_chats() -> list:
    chats = await chatsdb.find({}, {"chat_id": 1, "_id": 0}).to_list(length=None)
    return [chat["chat_id"] for chat in chats]
