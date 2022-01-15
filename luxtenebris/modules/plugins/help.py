from pyrogram import Client, filters
from .misc.registry import plugins_and_help, command_prefix

plugins_and_help['help_no_module'] = f"No valid **module** was specified, please provide **module** name: \n`{command_prefix}help [module]`"

@Client.on_message(filters.command('help', command_prefix))
async def command_help(client, message):
    not_edited = True
    print(not_edited) # DEBUG
    for key in plugins_and_help:
        if key in message.text.lower() and not_edited == True:
            print(f'Showing help for {key}...') # DEBUG LOG STUFF
            not_edited = False
            await message.edit(plugins_and_help[key])
    if not_edited is True:
        await message.edit(plugins_and_help['help_no_module'])
