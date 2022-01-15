from pyrogram import Client, filters
from ..registry import plugins_and_help, command_prefix

plugins_and_help['image'] = '**PLACEHOLDER**'

@Client.on_message()
async def command_image(client, message):
    print(message)
    await message.edit("123")