from pyrogram import filters
from modules.clients.main_user import user

chats_involved = []

@user.on_message(filters.text & filters.private)
async def command_echo(client, message):
    await message.reply(message)