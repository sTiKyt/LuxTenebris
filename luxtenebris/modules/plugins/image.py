from pyrogram import Client, filters
from ..registry import plugins_and_help, command_prefix

plugins_and_help['image'] = '**PLACEHOLDER**'

@Client.on_message(filters.command('image', command_prefix))
async def command_image(client, message):
    await message.reply('test')