from os import path
from PIL import Image
from pyrogram import Client, filters
from .misc.registry import plugins_and_help, command_prefix

from os import getcwd

plugins_and_help['image'] = '**PLACEHOLDER**'

@Client.on_message(filters.reply & filters.command(['image', 'img'], command_prefix))
async def command_image(client, message):
    message_text = str(message.text)
    media = f'{path.dirname(__file__)}/temp/{message.reply_to_message.message_id}'
    try:
        await client.download_media(message.reply_to_message, file_name=media)
        img = Image.open(media)
        print(img.format) # DEBUG
        await message.edit(f"This is **{img.format}** image, **converting to .png**...")
        rgba = img.convert("RGBA")
        rgba.save(f'{media}.png', 'png')
        await client.send_document(chat_id=message.chat.id, document=f'{media}.png', reply_to_message_id=message.message_id)
    except:
        await message.edit("This is **NOT** an **image**!")
        print('Not an image!') # DEBUG 
    
    
    
    