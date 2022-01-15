import asyncio
from os import getcwd, path
from modules.clients.main_user import user
from pyrogram import filters

from modules.commands.echo import command_echo, execute_echo

def login():
    if path.exists("./config.ini"):
        print('Credentials config found')
    else:
        print("Login at https://my.telegram.org/apps and")
        api_id = int(input("enter your api_id: "))
        api_hash = input("enter your api_hash: ")
        with open(f'{str(__file__).replace("main.py", "")}/config.ini', 'w') as config: # I know this line looks like shit, fuck off
            config.write(f"[pyrogram] \n api_id = {api_id} \n api_hash = {api_hash}")

if __name__ == "__main__":
    login()
    user.run()
