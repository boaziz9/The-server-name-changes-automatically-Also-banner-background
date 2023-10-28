import discord
import os
import requests
import asyncio
import random

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

server_id = "" # ايدي سيرفرك دسكورد
background_images = [
    "https://i.pinimg.com/564x/83/1e/0a/831e0a83beee7a593506fc5e0af1926a.jpg", # صورة رقم 1
    "https://i.pinimg.com/564x/21/d5/c3/21d5c3f82da3b10e674c19cf799dc78e.jpg", # صورة رقم 2
    "https://i.pinimg.com/564x/f4/70/cf/f470cf131163cecb39c61ac0d5d114ab.jpg" # صورة رقم 3
]

async def change_background():
    while True:
        background_image_url = random.choice(background_images)
        server = client.get_guild(int(server_id))
        if server is not None:
            with open("background.jpg", "wb") as background_file:
                background_data = requests.get(background_image_url).content
                background_file.write(background_data)
            with open("background.jpg", "rb") as background_file:
                await server.edit(banner=background_file.read())
        await asyncio.sleep(1)

async def change_server_name():
    server = client.get_guild(int(server_id))
    server_names = [
        "Slt3 Discord",
        "Free Nitro",
        "Slt3 Discord",
        "Free Rdp",
        "Slt3 Discord",
        "Fivem Discord",
        "Slt3 Discord",
        "Curse LTD",
        "Slt3 Discord",
        "Curse Discord"
    ]
    while True:
        for name in server_names:
            if server is not None:
                await server.edit(name=name)
            await asyncio.sleep(1)

@client.event
async def on_ready():
    print(f'Done {client.user.name}')
    client.loop.create_task(change_background())
    client.loop.create_task(change_server_name())


client.run("")  # توكن البوت
