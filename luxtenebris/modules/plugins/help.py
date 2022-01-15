from pyrogram import Client, filters
from ..registry import plugins_and_help, command_prefix

plugins_and_help['help_no_module'] = f"No valid **module** was specified, please provide **module** name: \n`{command_prefix}help [module]`"

@Client.on_message(filters.command('help', command_prefix))
async def command_help(client, message):
    for key in plugins_and_help:
        if key in message.text.lower():
            print(f'Showing help for {key}...') # DEBUG LOG STUFF
            await message.edit(plugins_and_help[key])
        else:
            try:
                await message.edit(plugins_and_help['help_no_module'])
            except:
                print("Message was already edited, skipping") #DEBUG LOG
