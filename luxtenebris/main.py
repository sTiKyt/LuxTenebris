import asyncio
from os import getcwd, path
from pyrogram import Client

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

if __name__ == "__main__":
    login()
    #asyncio.run(main())