from os import path
from PIL import Image
from pyrogram import Client, filters
from .misc.registry import plugins_and_help, command_prefix

from os import getcwd

extensions = ['png','webp','jpeg']
plugins_and_help['image'] = f"""
**== Manipulate images and stickers ==**
```Usage: `{command_prefix}image [option]`
Options:
convert [extension]: convert to specified extension
                     Extensions:
                        {', '.join(extensions)}
as_file            : returns image as file, 
                     without compression```"""

@Client.on_message(filters.reply & filters.command(['image', 'img'], command_prefix))
async def command_image(client, message):
    message_text = str(message.text)
    media = f'{path.dirname(__file__)}/temp/{message.reply_to_message.message_id}'
    if "convert" in message_text.lower():
        for extension in extensions:
            if extension in message_text.lower(): 
                if 'webp' in extension:
                    message_text = f'{str(message.text)} as_file'
                try:
                    await client.download_media(message.reply_to_message, file_name=media)
                    img = Image.open(media)
                    print(img.format) # DEBUG
                    await message.edit(f"This is **{img.format}** image, **converting to .{extension}**...")
                    if "as_file" in message_text.lower():
                        if 'jpeg' in extension:
                            img = img.convert("RGB")
                        else:
                            img = img.convert("RGBA")
                        img.save(f'{media}.{extension}', extension)
                        await client.send_document(chat_id=message.chat.id, document=f'{media}.{extension}', reply_to_message_id=message.message_id)
                    else:
                        img = img.convert("RGB")
                        img.save(f'{media}.{extension}', extension)
                        await client.send_photo(chat_id=message.chat.id, photo=f'{media}.{extension}', reply_to_message_id=message.message_id)
                except:
                    await message.edit("This is **NOT** an **image**!")
                    print('Not an image!') # DEBUG 
    
    
    
    