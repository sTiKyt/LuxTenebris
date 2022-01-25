from pyrogram import Client, filters
from .misc.registry import plugins_and_help, command_prefix
from simplejson import loads
from yaml import dump
import re

plugins_and_help['debug'] = "Placeholder, blah, blah, blah"

@Client.on_message(filters.command('debug', command_prefix))
async def command_debug(client, message):
    message_text = str(message.text)
    if "message" in message_text.lower():
        data = message
    try:
        yaml_message = dump(loads(str(data).encode("utf-8")), default_flow_style=False)
    except:
        yaml_message = "You should be specifying some shit, you know?.."
    unicode_fixed = re.sub(r'\\u([0-9a-fA-F]{4})',lambda m: chr(int(m.group(1),16)),yaml_message)
    await message.reply(unicode_fixed)

# TODO add more, add help, make it harder, better, faster