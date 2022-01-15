from random import uniform
from asyncio import sleep
from pyrogram import Client, filters
from modules.clients.main_user import command_prefix
from ..registry import plugins_and_help

plugins_and_help['echo'] = f"""
**== Repeat messages after others ==**
```Usage: `{command_prefix}echo [option]`
Options:
true, enable   : activate echo mode
false, disable : deactivate echo mode
loop, kill     : repeats all messages it can see
                 indefinitely, requires further
                 confirmation for your accounts
                 safety but can be bypassed by
                 confirming it ahead of time```"""

chats_involved = {}
loop = False

@Client.on_message(filters.command('echo', command_prefix))
async def command_echo(client, message) -> None:
    """Enable repeating of all incoming messages in chat

    Args:
        client ([Client]): Pyrogram client, usually passed by decorator
        message ([Message]): Pyrogram message, usually passed by decorator
    """
    global loop
    chat_data = await client.get_chat(message.chat.id)
    chat_name = f'**{chat_data.title}**'
    data = str(message.text)
    if "enable" in data.lower() or "true" in data.lower():
        chats_involved[message.chat.id] = 1
        await message.edit(f"Module **echo** was enabled in {chat_name}")
    elif "disable" in data.lower() or "false" in data.lower():
        chats_involved[message.chat.id] = 0
        loop = False
        await message.edit(f"Module **echo** was disabled in {chat_name}")
    elif ("loop" in data.lower() or "kill" in data.lower()) and "YES" in data:
        loop = True
        await message.edit(f"**Loop** mode of **echo** is **activated**! Run, fools!")
    elif "loop" in data.lower() or "kill" in data.lower():
        if loop == True:
            loop = not loop
        await message.edit(f"**Loop** mode is very dangerous and can get you **BANNED**, to confirm activation run: ```{command_prefix}echo loop YES```")
    try:
        if chats_involved[message.chat.id] == 0 and loop:
            await message.reply(f"Not really, you forgot to enable **echo**, genius... run: ```{command_prefix}echo true```")
    except:
        pass # TODO log some info or warning about chat not being in dictionary yet

    print(chats_involved) # REPLACE WITH DEBUGLOG
    print(message.chat.id) # DEBUG LOG
    #print(loop)

@Client.on_message()
async def execute_echo(client, message):
    global loop
    if message.chat.id not in chats_involved:
        chats_involved[message.chat.id] = 0
    if chats_involved[message.chat.id] == 1:
        if message.text is not f'{command_prefix}echo':
            if message.sticker is not None:
                while loop:
                    await message.reply_sticker(message.sticker.file_id)
                await message.reply_sticker(message.sticker.file_id)
                
            elif message.text is not None:
                print(loop) #DEBUG LOG
                while loop:
                    await sleep(uniform(uniform(1, 2), uniform(1, 2)))
                    await message.reply(message.text)
                await message.reply(message.text)
                # await message.reply(message) # FOR DEBUG


 