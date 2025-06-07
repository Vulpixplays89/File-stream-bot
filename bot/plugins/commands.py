#pylint:disable=E0602
from telethon import Button
from telethon.events import NewMessage
from telethon.tl.custom.message import Message
from bot import TelegramBot
from bot.config import Telegram
from bot.modules.static import *
from bot.modules.decorators import verify_user
from pymongo import MongoClient

# MongoDB setup
mongo_client = MongoClient("mongodb+srv://callbot:callbot@cluster0.a3lcyab.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Replace with your actual URI
db = mongo_client["filestream"]
users_col = db["users"]

@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/start$'))
@verify_user(private=True)
async def welcome(event: NewMessage.Event | Message):
    user_id = event.sender_id
    if not users_col.find_one({"user_id": user_id}):
        users_col.insert_one({"user_id": user_id})
    await event.reply(
        message=WelcomeText % {'first_name': event.sender.first_name},
    )

@TelegramBot.on(NewMessage(chats=Telegram.OWNER_ID, incoming=True, pattern=r'^/users$'))
async def list_users(event: NewMessage.Event | Message):
    count = users_col.count_documents({})
    user_ids = users_col.find({}, {"_id": 0, "user_id": 1})
    users = "\n".join([str(u["user_id"]) for u in user_ids])
    await event.reply(f"👥 Total Users: {count}\n\n{users}")

@TelegramBot.on(NewMessage(chats=Telegram.OWNER_ID, incoming=True, pattern=r'^/broadcast$'))
async def broadcast_handler(event: Message):
    if not event.is_reply:
        return await event.reply("❗Please reply to a message to broadcast.")
    
    reply_msg = await event.get_reply_message()
    user_ids = users_col.find({}, {"_id": 0, "user_id": 1})
    
    success = 0
    fail = 0
    for user in user_ids:
        try:
            await reply_msg.forward_to(user["user_id"])
            success += 1
        except Exception as e:
            fail += 1
        await asyncio.sleep(0.5)

    await event.reply(f"✅ Broadcast finished!\n\n✅ Sent: {success}\n❌ Failed: {fail}")



@TelegramBot.on(NewMessage(incoming=True, pattern=r'^/info$'))
@verify_user(private=True)
async def user_info(event: Message):
    await event.reply(UserInfoText.format(sender=event.sender))

@TelegramBot.on(NewMessage(chats=Telegram.OWNER_ID, incoming=True, pattern=r'^/log$'))
async def send_log(event: NewMessage.Event | Message):
    await event.reply(file='event-log.txt')
