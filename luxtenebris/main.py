import asyncio
from os import getcwd, path
from pyrogram import Client, filters

user = Client("LuxTenebris")

def login():
    if path.exists("./config.ini"):
        print('Credentials config found')
    else:
        print("Login at https://my.telegram.org/apps and")
        api_id = int(input("enter your api_id: "))
        api_hash = input("enter your api_hash: ")
        with open(f'{str(__file__).replace("main.py", "")}/config.ini', 'w') as config:
            config.write(f"[pyrogram] \n api_id = {api_id} \n api_hash = {api_hash}")

@user.on_message(filters.text & filters.private & filters.command(commands))
async def test_handler(client, message):
    await message.reply(message.text)


if __name__ == "__main__":
    login()
    user.run()